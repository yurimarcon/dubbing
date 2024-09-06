import os
import torch
from pydub import AudioSegment
from TTS.api import TTS
from utils_audio import get_silence_ranges, get_initial_silence_duration
from config import (
    VOICE_MODEL,
    SOURCE_FOLDER,
    TEMP_FOLDER,
    PATH_RELATIVE,
    FILE_NAME_SEGMENT,
    FILE_NAME_ADJUSTED_TEMP,
    FILE_NAME_ADJUSTED,
    ORIGINAL_AUDIO,
    OUTPUT_AUDIO
)

# Initialize TTS model
tts_model = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2", 
    progress_bar=False, 
    gpu=torch.cuda.is_available()
)

def get_files_path(idx):
    initial_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_SEGMENT}{idx}.wav")
    adjusted_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_ADJUSTED_TEMP}{idx}.wav")
    final_chunk_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_ADJUSTED}{idx}.wav")

    return initial_file, adjusted_file, final_chunk_file

def combine_adjusted_segments(segments, input_audio, dest_folder, output_file):
    final_audio = AudioSegment.silent(duration=get_initial_silence_duration(get_silence_ranges(input_audio)))
    for idx, segment in enumerate(segments):
        adjusted_audio = AudioSegment.from_file(os.path.join(dest_folder, f"{FILE_NAME_ADJUSTED}{idx}.wav"))
        final_audio += adjusted_audio
    final_audio.export(output_file, format="wav")

def generate_audio_by_text(text, speaker_wav, dest_path, source_lang, dest_language, tts_model=tts_model):
    text = translate_text(text, source_lang, dest_language) if dest_language != "en" else text
    tts_model.tts_to_file(
        text=text, 
        speaker_wav=speaker_wav, 
        language=dest_language, 
        file_path=dest_path
    )

def combine_audios_and_silences(original_audio, path_starts_with, silences_ranges, dest_folder):
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
            original_audio_duration = len(original_audio)
            final_audio_duration = len(final_audio)
            if final_audio_duration < original_audio_duration:
                last_segment = AudioSegment.from_file(f"{path_starts_with}{idx+1}.wav")
                final_audio += last_segment
        
    final_audio.export(dest_folder, format="wav")
        
    return final_audio