from repository.process_repository import create_process, get_process_by_id, update_process_by_relative_path, get_process_by_user_id
from datetime import datetime

def create_process_service(user_id, relative_path, source_lang, target_lang, original_file_name):
    return create_process(user_id, relative_path, source_lang, target_lang, original_file_name)

def get_audio_done_service(relative_path):
    process_to_update = {
        "relative_path": relative_path,
        "get_audio_done": "100%",
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

def split_audio_done_service(relative_path, quantity_split, atual_split):
    percent = (atual_split / quantity_split) * 100
    process_to_update = {
        "relative_path": relative_path,
        "split_audio_done": f"{round(percent)}%",
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    print(process_to_update)
    update_process_by_relative_path(process_to_update)

def transcript_done_service(relative_path, quantity_split, atual_split):
    percent = (atual_split / quantity_split) * 100
    process_to_update = {
        "relative_path": relative_path,
        "transcript_done": f"{round(percent)}%",
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

def create_audio_done_service(relative_path, quantity_split, atual_split):
    percent = (atual_split / quantity_split) * 100
    process_to_update = {
        "relative_path": relative_path,
        "create_audio_done": f"{round(percent)}%",
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

def unify_audio_done_service(relative_path):
    process_to_update = {
        "relative_path": relative_path,
        "unify_audio_done": "100%",
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

def record_silence_ranges(relative_path, silence_ranges):
    process_to_update = {
        "relative_path": relative_path,
        "silence_ranges": f"'{silence_ranges}'",
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

def record_quantity_split(relative_path, quantity_split):
    process_to_update = {
        "relative_path": relative_path,
        "quantity_split": quantity_split,
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

def record_download_file_name(relative_path, file_name):
    process_to_update = {
        "relative_path": relative_path,
        "download_file_name": file_name,
        "last_update":f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

def get_process_by_user_id_service(user_id):
    return get_process_by_user_id(user_id)
