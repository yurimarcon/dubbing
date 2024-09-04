import whisper
from TTS.api import TTS
import torch
from pydub import AudioSegment
import sys
import json
import os
import glob

from audio_utils import (
    get_silence_ranges, 
    get_initial_silence_duration, 
    get_speed_factory, 
    remove_silence_unecessery, 
    put_silence_to_ajust_time, 
    ajust_time_segments
)
from translate_utils import translate_text

# Paths and filenames
VOICE_MODEL = "model_voice/model.wav"
SOURCE_FOLDER = "result/"
TEMP_FOLDER = "temp/"
PATH_RELATIVE = os.path.join(SOURCE_FOLDER, TEMP_FOLDER)
FILE_NAME_SEGMENT = "segment_"
FILE_NAME_ADJUSTED_TEMP = "segment_ajusted_temp_"
FILE_NAME_ADJUSTED = "segment_ajusted_"
ORIGINAL_AUDIO = os.path.join(PATH_RELATIVE, "audio.wav")
OUTPUT_AUDIO = os.path.join(PATH_RELATIVE, "output.wav")

# Command line arguments
input_audio = sys.argv[1]
input_transcript_text = sys.argv[2]
output_audio = sys.argv[3]
source_lang = sys.argv[4]
dest_language = sys.argv[5]

# Initialize TTS model
tts_model = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2", 
    progress_bar=False, 
    gpu=torch.cuda.is_available()
)

def load_transcript(file_path):
    with open(file_path, 'r') as file:    
        return json.load(file)['segments']

def generate_audio_segments(segments, speaker_wav, dest_folder, tts_model):
    for idx, segment in enumerate(segments):
        text = translate_text(segment['text'], source_lang, dest_language) if dest_language != "en" else segment['text']
        tts_model.tts_to_file(
            text=text, 
            speaker_wav=speaker_wav, 
            language=dest_language, 
            file_path=os.path.join(dest_folder, f"{FILE_NAME_SEGMENT}{idx}.wav")
        )
        print(f"{idx + 1}/{len(segments)} segments created.")

def adjust_segment_speed(segment, initial_file, adjusted_file):
    speed_factor = get_speed_factory(segment, initial_file)
    os.system(f'ffmpeg -i {initial_file} -filter:a "atempo={speed_factor}" {adjusted_file}')

def combine_adjusted_segments(segments, dest_folder, output_file):
    final_audio = AudioSegment.silent(duration=get_initial_silence_duration(get_silence_ranges(input_audio)))
    for idx, segment in enumerate(segments):
        adjusted_audio = AudioSegment.from_file(os.path.join(dest_folder, f"{FILE_NAME_ADJUSTED}{idx}.wav"))
        final_audio += adjusted_audio
    final_audio.export(output_file, format="wav")

def clean_up_files(pattern):
    files = glob.glob(pattern)
    for file in files:
        os.remove(file)

def main():
    segments = load_transcript(input_transcript_text)

    generate_audio_segments(segments, input_audio, PATH_RELATIVE, tts_model)

    for idx, segment in enumerate(segments):
        initial_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_SEGMENT}{idx}.wav")
        adjusted_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_ADJUSTED_TEMP}{idx}.wav")
        final_chunk_file = os.path.join(PATH_RELATIVE, f"{FILE_NAME_ADJUSTED}{idx}.wav")
        
        adjust_segment_speed(segment, initial_file, adjusted_file)
        remove_silence_unecessery(adjusted_file)
        put_silence_to_ajust_time(segment, adjusted_file)
        adjust_segment_speed(segment, adjusted_file, final_chunk_file)

    combine_adjusted_segments(segments, PATH_RELATIVE, OUTPUT_AUDIO)
    ajust_time_segments(ORIGINAL_AUDIO, OUTPUT_AUDIO)
    # clean_up_files(os.path.join(PATH_RELATIVE, "segment*"))

if __name__ == "__main__":
    main()
