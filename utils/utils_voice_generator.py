import os
import torch
import json
import shutil
from pydub import AudioSegment
from TTS.api import TTS
from utils.utils_audio import get_silence_ranges, get_initial_silence_duration, ajust_speed_audio, create_silence
from utils.utils_translate import translate_text
from utils.utils_loger import log_error, log_info
from services.process_service import create_audio_done_service
from config import (
    VOICE_MODEL,
    PATH_RELATIVE,
    FILE_NAME_SEGMENT,
    FILE_NAME_ADJUSTED_TEMP,
    FILE_NAME_ADJUSTED,
    ORIGINAL_AUDIO,
    OUTPUT_AUDIO
)

def initialize_tts_model():
    # Initialize TTS model
    tts_model = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2", 
        progress_bar=False, 
        gpu=torch.cuda.is_available()
    )
    return tts_model

def get_files_path(idx):
    initial_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_SEGMENT}{idx}.wav")
    adjusted_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_ADJUSTED_TEMP}{idx}.wav")
    final_chunk_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_ADJUSTED}{idx}.wav")

    return initial_file, adjusted_file, final_chunk_file

def combine_adjusted_segments(segments, temp_file_name, output_file):
    final_audio = AudioSegment.silent(duration=0)
    for idx, segment in enumerate(segments):
        adjusted_audio = AudioSegment.from_file(f"{temp_file_name}{idx}.wav")
        final_audio += adjusted_audio
    final_audio.export(output_file, format="wav")

    # Record log with name and time duration sniped audio
    video_duration = AudioSegment.from_file(output_file)
    log_info(f"{output_file} {len(video_duration)}")

def generate_audio_by_text(text, speaker_wav, dest_path, source_lang, dest_language, tts_model):
    text_tractabled = translate_text(text, source_lang, dest_language) if dest_language != "en" else text
    try:
        tts_model.tts_to_file(
            text=text_tractabled, 
            speaker_wav=speaker_wav, 
            language=dest_language, 
            file_path=dest_path
        )
    except Exception as e:
        log_error(f"{speaker_wav} {dest_language} {dest_path} Error: {e}")
        tts_model.tts_to_file(
            text=text, 
            speaker_wav=speaker_wav,
            language=dest_language, 
            file_path=dest_path
        )
        print(e)

def combine_audios_and_silences(original_audio_path, path_starts_with, silences_ranges, relative_path, path_output_audio):

    if len(silences_ranges) == 0:
        shutil.copy(f"{relative_path}/segment_ajusted_0.wav", path_output_audio)
        return AudioSegment.from_file(path_output_audio)
    else:
        final_audio = AudioSegment.silent(duration=0)
        for idx, silence in enumerate(silences_ranges):
            silence_duration = (silence[1] - silence[0]) * 1000
            audio_silence = AudioSegment.silent(duration=round(silence_duration))

            # if audio finish with silence enter here
            if not os.path.exists(f"{path_starts_with}{idx}.wav"):
                final_audio += audio_silence
                break

            audio_segment = AudioSegment.from_file(f"{path_starts_with}{idx}.wav")

            # if is first loop enter here
            if silence[0] == 0:
                audio_silence += audio_segment
                final_audio += audio_silence
            else:
                audio_segment += audio_silence
                final_audio += audio_segment

            # verify if is last loop
            if idx+1 == len(silences_ranges):
                original_audio = AudioSegment.from_file(original_audio_path)
                original_audio_duration = len(original_audio)
                final_audio_duration = len(final_audio)
                if final_audio_duration < original_audio_duration:
                    if os.path.exists(f"{path_starts_with}{idx+1}.wav"):
                        last_segment = AudioSegment.from_file(f"{path_starts_with}{idx+1}.wav")
                        final_audio += last_segment
            
        final_audio.export(path_output_audio, format="wav")
        
    return final_audio

def get_speaker_path(relative_path, idx, model_speaker_path):
    if model_speaker_path:
        return model_speaker_path

    speaker_path = f"{relative_path}/audio_{idx}.wav"
    audio_speaker = AudioSegment.from_file(speaker_path)
    min_duration_audio = 3000 # in miliseconds
    if len(audio_speaker) < min_duration_audio:

        # Verify next 3 audios if has more duration
        for s in range(3):
            temp_speaker_path = f"{relative_path}/audio_{idx + s}.wav"
            if os.path.exists(temp_speaker_path):
                audio_temp_speaker = AudioSegment.from_file(temp_speaker_path)
                if len(audio_temp_speaker) > len(audio_speaker):
                    speaker_path = temp_speaker_path
                    audio_speaker = AudioSegment.from_file(speaker_path)
            else:
                break

        # if did find a audio duration Ok, can return
        if len(audio_speaker) > min_duration_audio:
            return speaker_path
        
         # Verify last 3 audios if has more duration
        for s in range(3):
            temp_speaker_path = f"{relative_path}audio_{idx - s}.wav"
            if os.path.exists(temp_speaker_path):
                audio_temp_speaker = AudioSegment.from_file(temp_speaker_path)
                if len(audio_temp_speaker) > len(audio_speaker):
                    speaker_path = temp_speaker_path
                    audio_speaker = AudioSegment.from_file(speaker_path)
            else:
                break
    return speaker_path

def create_segments_in_lot(quantity_sliced_audios, source_lang, dest_lang, relative_path, tts_model):
    
    # It happends when audio has any silence and is just one audio
    if quantity_sliced_audios == 0:
        quantity_sliced_audios = 1


    for idx in range(quantity_sliced_audios):
        print(f"{idx}/{quantity_sliced_audios}")
        create_audio_done_service(relative_path, quantity_sliced_audios, idx+1)

        with open(f"{relative_path}/transcript_{idx}.json", 'r') as file:    
            segments = json.load(file)['segments']

        # speaker_model_path = f"result/temp/yuri/2024-09-18-11-25-01/audio_16.wav"
        # speaker_model_path = f"model_voice/model.wav"
        speaker_model_path = f""
        speaker_wav = get_speaker_path(relative_path, idx, speaker_model_path)
        print("speaker_wav ++>>",speaker_wav)

        # generate segments to each transcript
        for idy, segment in enumerate(segments):
            print(f"{idy}/{len(segments)} from {idx}/{quantity_sliced_audios}")
            if len(segment['text']) == 0:
                # Create a silence of 1 minut
                create_silence(0, 1, f"{relative_path}/segment_{idx}_{idy}.wav")
            elif segment['text'] == " Music" or segment['text'] == " Applause":
                # Create a silence if the segment is about Music an has not text
                create_silence(segment['start'], segment['end'], f"{relative_path}/segment_{idx}_{idy}.wav")
            else:
                generate_audio_by_text(
                    segment['text'], 
                    speaker_wav, 
                    f"{relative_path}/segment_{idx}_{idy}.wav", 
                    source_lang, 
                    dest_lang,
                    tts_model
                    )
        # combine segments to create one segment by transcript
        combine_adjusted_segments(
            segments, 
            f"{relative_path}/segment_{idx}_",
            f"{relative_path}/segment_{idx}.wav"
            )
            
        # Ajust speed audio by segment
        ajust_speed_audio(
            f"{relative_path}/segment_{idx}.wav", 
            f"{relative_path}/audio_{idx}.wav",
            f"{relative_path}/segment_ajusted_{idx}.wav"
            )
