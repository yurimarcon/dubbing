from pydub import AudioSegment
import os
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