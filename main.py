from config import ORIGINAL_AUDIO, PATH_RELATIVE
from utils_audio import extract_audio_from_video, detect_silences, ajust_speed_audio
from utils_voice_generator import generate_audio_by_text, combine_audios_and_silences, combine_adjusted_segments, create_segments_in_lot
from splitter_audio import cut_video_at_silence
import sys
import os
import json
import glob

def create_transcript(quantity_sliced_audios):
    for idx in range(quantity_sliced_audios):
        os.system(
            f"python transcript.py {PATH_RELATIVE}audio_{idx}.wav translate {PATH_RELATIVE}transcript_{idx}.json en pt")

def combine_segments(silence_intervals):
    combine_audios_and_silences(
        ORIGINAL_AUDIO, 
        f"{PATH_RELATIVE}/segment_ajusted_",
        silence_intervals,
        f"{PATH_RELATIVE}/pre_output.wav"
        )
    ajust_speed_audio(
            f"{PATH_RELATIVE}pre_output.wav", 
            f"{PATH_RELATIVE}1_audio.wav",
            f"{PATH_RELATIVE}output.wav"
            )
    
def combine_result_audio_with_video(initial_video):
    os.system(
        f"ffmpeg -i {initial_video} \
            -i {PATH_RELATIVE}output.wav \
            -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
            -shortest result/result.mp4"
    )

def clean_up(relative_path):
    all_file = glob.glob(os.path.join(relative_path, "*"))
    os.remove(all_file)

def main():
    VIDEO_PATH = sys.argv[1]

    extract_audio_from_video(VIDEO_PATH, ORIGINAL_AUDIO)
    silence_intervals = detect_silences(ORIGINAL_AUDIO)
    quantity_sliced_audios = cut_video_at_silence(ORIGINAL_AUDIO, silence_intervals, PATH_RELATIVE)
    create_transcript(quantity_sliced_audios)
    create_segments_in_lot(
        quantity_sliced_audios,
        PATH_RELATIVE
        )
    combine_segments(silence_intervals)
    combine_result_audio_with_video(VIDEO_PATH)
    clean_up(PATH_RELATIVE)

if __name__ == "__main__":
    main()