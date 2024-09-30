from config import ORIGINAL_AUDIO_NAME, TEMP_ORIGINAL_AUDIO_NAME
from utils.utils_audio import extract_audio_from_video, detect_silences, ajust_speed_audio
from utils.utils_voice_generator import combine_audios_and_silences, create_segments_in_lot
from utils.utils_splitter_audio import cut_video_at_silence
from utils.utils_transcript import build_trancript
from utils.utils_loger import log_info
from utils.utils_noise_reduce import noise_reduce
from utils.utils_voice_generator import initialize_tts_model
from services.process_service import create_process_service, get_audio_done_service, split_audio_done_service, transcript_done_service, create_audio_done_service, unify_audio_done_service, record_quantity_split, record_silence_ranges, record_download_file_name
from utils.utils_get_frame import get_frame

import sys
import os
import json
import glob
import shutil
from datetime import datetime
import subprocess

import concurrent.futures

def process_audio(idx, relative_path, source_lang, quantity_sliced_audios):
    # Atualiza o progresso da transcrição
    transcript_done_service(relative_path, quantity_sliced_audios, idx + 1)
    
    # Constrói a transcrição do áudio
    build_trancript(
        os.path.join(relative_path, f"audio_{idx}.wav"), 
        source_lang, 
        os.path.join(relative_path, f"transcript_{idx}.json")
    )

def create_transcript(quantity_sliced_audios, source_lang, dest_lang, relative_path):
    if quantity_sliced_audios == 0:
        build_trancript(
            os.path.join(relative_path, "audio_0.wav"), 
            source_lang, 
            os.path.join(relative_path, "transcript_0.json")
        )
        return

    # Utiliza paralelismo para melhorar o desempenho
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Agenda todas as transcrições para execução paralela
        futures = [
            executor.submit(process_audio, idx, relative_path, source_lang, quantity_sliced_audios) 
            for idx in range(quantity_sliced_audios)
        ]

        # Aguarda a conclusão de todas as tarefas, lidando com exceções, se houver
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Pode capturar exceções e tratá-las aqui
            except Exception as exc:
                print(f"Erro durante o processamento do áudio: {exc}")

# def create_transcript(quantity_sliced_audios, source_lang, dest_lang, relative_path):
#     if quantity_sliced_audios == 0:
#         build_trancript(
#             os.path.join(relative_path, "audio_0.wav"), 
#             source_lang, 
#             os.path.join(relative_path, "transcript_0.json")
#             )
#         return

#     for idx in range(quantity_sliced_audios):
        
#         transcript_done_service(relative_path, quantity_sliced_audios, idx+1)

#         build_trancript(
#             os.path.join(relative_path, f"audio_{idx}.wav"), 
#             source_lang, 
#             os.path.join(relative_path, f"transcript_{idx}.json")
#             )

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
    command = [
        "ffmpeg", 
        "-i", initial_video, 
        "-i", os.path.join(relative_path, "output.wav"), 
        "-c:v", "copy", 
        "-c:a", "aac", 
        "-map", "0:v:0", 
        "-map", "1:a:0",
        "-shortest", os.path.join(relative_path, "result.mp4")
    ]
    subprocess.run(command, check=True)

    # os.system(
    #     f"ffmpeg -i {initial_video} \
    #         -i {relative_path}/output.wav \
    #         -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
    #         -shortest {relative_path}/result.mp4"
    # )

def clean_up(relative_path):
    all_file = glob.glob(os.path.join(relative_path, "*"))
    for file in all_file:
        os.remove(file)

def  main(VIDEO_PATH, source_lang, dest_lang, relative_path, tts_model, user_id):
    log_info("main.py started...")
    log_info(f"VIDEO_PATH: {VIDEO_PATH} source_lang: {source_lang} dest_lang: {dest_lang} relative_path: {relative_path}")

    
    path_temp_original_audio = extract_audio_from_video(VIDEO_PATH, relative_path, TEMP_ORIGINAL_AUDIO_NAME)
    path_original_audio = noise_reduce(path_temp_original_audio, os.path.join(relative_path, ORIGINAL_AUDIO_NAME))
    # path_original_audio = f"result/admin/30-09-2024-14/39/31/1_audio.wav"
    get_audio_done_service(relative_path)

    silence_intervals = detect_silences(path_original_audio)
    record_silence_ranges(relative_path, silence_intervals)
    log_info(silence_intervals)

    quantity_sliced_audios = cut_video_at_silence(path_original_audio, silence_intervals, relative_path)
    log_info("quantity_sliced_audios")
    log_info(f"quantity_sliced_audios: {quantity_sliced_audios}")
    record_quantity_split(relative_path, quantity_sliced_audios)

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
    unify_audio_done_service(relative_path)
    record_download_file_name(relative_path, "result.mp4")
    # clean_up(relative_path)

if __name__ == "__main__":
    
    # if main.py did called diretly without API, will be enter in this if
    if __name__ == "__main__":
        VIDEO_PATH = sys.argv[1]
        source_lang = sys.argv[2]
        target_lang = sys.argv[3]
        relative_path = sys.argv[4]
        tts_model = initialize_tts_model()
        user_id = 1
        original_file_name = "t.mp4"

        relative_path = os.path.join(relative_path, "admin", datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        if not os.path.exists(relative_path):
            os.makedirs(relative_path) 

        get_frame(VIDEO_PATH, os.path.join(relative_path, "tumbnail.jpg"))

        create_process_service(user_id, relative_path, source_lang, target_lang, original_file_name)

    main(VIDEO_PATH, source_lang, target_lang, relative_path, tts_model, user_id)