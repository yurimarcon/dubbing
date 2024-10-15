from repository.process_repository import create_process, get_process_by_id, update_process_by_relative_path, get_process_by_user_id
from repository.dynamo_process_repository import update_field_repository
from datetime import datetime

PK = ""
SK = ""

def set_PK_and_SK_to_update_dynamo(processObject):
    global PK
    global SK
    if processObject['PK'] != "":
        PK = processObject['PK'] 
        SK = processObject['SK'] 

def set_start_process_service():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            2
        )

def create_process_service(user_id, relative_path, source_lang, target_lang, original_file_name):
    return create_process(user_id, relative_path, source_lang, target_lang, original_file_name)

def get_audio_done_service(relative_path):
    process_to_update = {
        "relative_path": relative_path,
        "get_audio_done": "100%",
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'get_audio_done',
            '100%'
        )

def split_audio_done_service(relative_path, quantity_split, atual_split):
    percent = (atual_split / quantity_split) * 100
    process_to_update = {
        "relative_path": relative_path,
        "split_audio_done": f"{round(percent)}%",
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    print(process_to_update)
    update_process_by_relative_path(process_to_update)

    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'split_audio_done',
            f"{round(percent)}%" 
        )

def transcript_done_service(relative_path, quantity_split, atual_split):
    percent = (atual_split / quantity_split) * 100
    process_to_update = {
        "relative_path": relative_path,
        "transcript_done": f"{round(percent)}%",
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'transcript_audio_done',
            f"{round(percent)}%" 
        )

def create_audio_done_service(relative_path, quantity_split, atual_split):
    percent = (atual_split / quantity_split) * 100
    process_to_update = {
        "relative_path": relative_path,
        "create_audio_done": f"{round(percent)}%",
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'create_audio_done',
            f"{round(percent)}%" 
        )

def unify_audio_done_service(relative_path):
    process_to_update = {
        "relative_path": relative_path,
        "unify_audio_done": "100%",
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'unify_audio_done',
            '100%'
        )

def record_silence_ranges(relative_path, silence_ranges):
    process_to_update = {
        "relative_path": relative_path,
        "silence_ranges": f"'{silence_ranges}'",
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'silence_ranges',
            silence_ranges
        )

def record_quantity_split(relative_path, quantity_split):
    process_to_update = {
        "relative_path": relative_path,
        "quantity_split": quantity_split,
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)

    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'quantity_split',
            quantity_split
        )

def record_download_file_name(relative_path, file_name):
    process_to_update = {
        "relative_path": relative_path,
        "download_file_name": file_name,
        "last_update":f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    }
    update_process_by_relative_path(process_to_update)
    
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'download_file_name',
            file_name
        )



def set_process_geting_audio():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            3
        )

def set_process_tracting_audio():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            4
        )

def set_process_spliting():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            5
        )

def set_process_transcripting():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            6
        )

def set_process_creating_audio():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            7
        )

def set_process_unifyng_audio():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            8
        )

def set_process_success():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            9
        )

def set_process_errror():
    if PK != "":
        #DynamoDB
        update_field_repository(
            PK,
            SK,
            'status',
            10
        )

def get_process_by_user_id_service(user_id):
    return get_process_by_user_id(user_id)
