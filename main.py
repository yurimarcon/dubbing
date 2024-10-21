from config import ORIGINAL_AUDIO_NAME, TEMP_ORIGINAL_AUDIO_NAME
from utils.utils_audio import extract_audio_from_video, detect_silences, ajust_speed_audio, separete_audio_and_background
from utils.utils_voice_generator import combine_audios_and_silences, create_segments_in_lot
from utils.utils_splitter_audio import cut_video_at_silence
from utils.utils_transcript import build_trancript
from utils.utils_loger import log_info
from utils.utils_noise_reduce import noise_reduce
from utils.utils_voice_generator import initialize_tts_model
from services.process_service import create_process_service, get_audio_done_service, split_audio_done_service, transcript_done_service, create_audio_done_service, unify_audio_done_service, record_quantity_split, record_silence_ranges, record_download_file_name, set_process_geting_audio, set_process_tracting_audio, set_process_spliting, set_process_transcripting, set_process_creating_audio, set_process_unifyng_audio, set_process_success
from utils.utils_get_frame import get_frame

import sys
import os
import json
import glob
import shutil
from datetime import datetime
import subprocess

def create_transcript(quantity_sliced_audios, source_lang, dest_lang, relative_path):

    if quantity_sliced_audios == 0:
        build_trancript(
            os.path.join(relative_path, "audio_0.wav"), 
            source_lang, 
            os.path.join(relative_path, "transcript_0.json")
            )
        transcript_done_service(relative_path, 1, 1) # It set 100% in step trancript.
        return

    for idx in range(quantity_sliced_audios):

        transcript_done_service(relative_path, quantity_sliced_audios, idx+1)
        
        if os.path.exists(os.path.join(relative_path, f"transcript_{idx}.json")):
            print("Do not need create transcript.")
            continue

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
    
def combine_result_audio_with_video(initial_video, relative_path, dest_lang):
    command = [
        "ffmpeg", 
        "-y",
        "-i", initial_video, 
        "-i", os.path.join(relative_path, "output.wav"), 
        "-c:v", "copy", 
        "-c:a", "aac", 
        "-map", "0:v:0", 
        "-map", "1:a:0",
        "-shortest", os.path.join(relative_path, "pre_output_video.mp4")
    ]
    subprocess.run(command, check=True)

def combine_audio_and_add_background(initial_video, relative_path, dest_lang):

    command = [
        "ffmpeg",
        "-i",
        initial_video,
        "-i",
        os.path.join(relative_path, "output.wav"),
        "-i",
        os.path.join(relative_path, "bg_audio.wav"),
        "-filter_complex",
        "[1:a][2:a]amix=inputs=2:duration=first:dropout_transition=3",
        "-c:v",
        "copy",
        "-map",
        "0:v",
        "-c:a",
        "aac",
        "-strict",
        "experimental",
        os.path.join(relative_path, f"{os.path.basename(initial_video)}_{dest_lang}.mp4")
    ]
    subprocess.run(command, check=True)


def  main(VIDEO_PATH, source_lang, dest_lang, relative_path, tts_model, user_id):
    log_info("main.py started...")
    log_info(f"VIDEO_PATH: {VIDEO_PATH} source_lang: {source_lang} dest_lang: {dest_lang} relative_path: {relative_path}")
    
    set_process_geting_audio()
    # temp_original_audio = extract_audio_from_video(VIDEO_PATH, relative_path, TEMP_ORIGINAL_AUDIO_NAME)
    temp_original_audio = separete_audio_and_background(VIDEO_PATH, relative_path)

    set_process_tracting_audio()
    path_original_audio = noise_reduce(temp_original_audio, os.path.join(relative_path, ORIGINAL_AUDIO_NAME))
    get_audio_done_service(relative_path)

    set_process_spliting()
    silence_intervals = detect_silences(path_original_audio)
    record_silence_ranges(relative_path, silence_intervals)
    log_info(silence_intervals)

    quantity_sliced_audios = cut_video_at_silence(path_original_audio, silence_intervals, relative_path)
    log_info(f"quantity_sliced_audios: {quantity_sliced_audios}")
    record_quantity_split(relative_path, quantity_sliced_audios)

    set_process_transcripting()
    create_transcript(quantity_sliced_audios, source_lang, dest_lang, relative_path)

    set_process_creating_audio()
    create_segments_in_lot(
        quantity_sliced_audios,
        source_lang,
        dest_lang,
        relative_path,
        tts_model
        )

    set_process_unifyng_audio()
    combine_segments(silence_intervals, relative_path, path_original_audio)
    # combine_result_audio_with_video(VIDEO_PATH, relative_path, dest_lang)
    combine_audio_and_add_background(VIDEO_PATH, relative_path, dest_lang)
    unify_audio_done_service(relative_path)
    record_download_file_name(relative_path, f"{os.path.basename(VIDEO_PATH)}_{dest_lang}.mp4")

    set_process_success()

if __name__ == "__main__":
    
    # if main.py did called diretly without API, will be enter in this if
    if __name__ == "__main__":
        VIDEO_PATH = sys.argv[1]
        source_lang = sys.argv[2]
        target_lang = sys.argv[3]
        relative_path = sys.argv[4]
        tts_model = initialize_tts_model()
        user_id = 1
        original_file_name = os.path.basename(VIDEO_PATH)

        relative_path = os.path.join(relative_path, "admin", datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
        if not os.path.exists(relative_path):
            os.makedirs(relative_path) 

        get_frame(VIDEO_PATH, os.path.join(relative_path, "thumbnail.jpg"))

        create_process_service(user_id, relative_path, source_lang, target_lang, original_file_name)

        main(VIDEO_PATH, source_lang, target_lang, relative_path, tts_model, user_id)
