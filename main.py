from config import ORIGINAL_AUDIO_NAME
from utils.utils_audio import extract_audio_from_video, detect_silences, ajust_speed_audio
from utils.utils_voice_generator import combine_audios_and_silences, create_segments_in_lot
from utils.utils_splitter_audio import cut_video_at_silence
from utils.utils_transcript import build_trancript
from utils.utils_loger import log_info

import sys
import os
import json
import glob
import shutil

def create_transcript(quantity_sliced_audios, source_lang, dest_lang, relative_path):
    if quantity_sliced_audios == 0:
        build_trancript(
            os.path.join(relative_path, "audio_0.wav"), 
            source_lang, 
            os.path.join(relative_path, "transcript_0.json")
            )
        return

    for idx in range(quantity_sliced_audios):
        build_trancript(
            os.path.join(relative_path, f"audio_{idx}.wav"), 
            source_lang, 
            os.path.join(relative_path, f"transcript_{idx}.json")
            )

def combine_segments(silence_intervals, relative_path, path_original_audio):
    
    combine_audios_and_silences(
        path_original_audio, 
        f"{relative_path}/segment_ajusted_",
        silence_intervals,
        relative_path,
        f"{relative_path}/pre_output.wav"
        )
            
    ajust_speed_audio(
            f"{relative_path}/pre_output.wav",
            f"{relative_path}/1_audio.wav",
            f"{relative_path}/output.wav"
            )
    
def combine_result_audio_with_video(initial_video, relative_path):
    os.system(
        f"ffmpeg -i {initial_video} \
            -i {relative_path}/output.wav \
            -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
            -shortest {relative_path}/result.mp4"
    )

def clean_up(relative_path):
    all_file = glob.glob(os.path.join(relative_path, "*"))
    for file in all_file:
        os.remove(file)

def  main(VIDEO_PATH, source_lang, dest_lang, relative_path, tts_model):
    log_info("main.py started...")
    log_info(f"VIDEO_PATH: {VIDEO_PATH} source_lang: {source_lang} dest_lang: {dest_lang} relative_path: {relative_path}")

    # if main.py did called diretly without API, will be enter in this if
    if __name__ == "__main__":
        VIDEO_PATH = sys.argv[1]
        source_lang = sys.argv[2]
        dest_lang = sys.argv[3]
        tts_model = sys.argv[4]

    path_original_audio = extract_audio_from_video(VIDEO_PATH, relative_path, ORIGINAL_AUDIO_NAME)
    silence_intervals = detect_silences(path_original_audio)
    log_info(silence_intervals)
    quantity_sliced_audios = cut_video_at_silence(path_original_audio, silence_intervals, relative_path)
    log_info("quantity_sliced_audios")
    log_info(f"quantity_sliced_audios: {quantity_sliced_audios}")
    create_transcript(quantity_sliced_audios, source_lang, dest_lang, relative_path)
    create_segments_in_lot(
        quantity_sliced_audios,
        source_lang,
        dest_lang,
        relative_path,
        tts_model
        )
    combine_segments(silence_intervals, relative_path, path_original_audio)
    combine_result_audio_with_video(VIDEO_PATH, relative_path)
    # clean_up(relative_path)

if __name__ == "__main__":
    main()