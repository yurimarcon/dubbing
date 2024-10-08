from  sqlite4  import  SQLite4
from entities.process import Process
from datetime import datetime

database = SQLite4("database.db")

database.connect()

def create_process(user_id, relative_path, source_lang, target_lang, original_file_name ):
    print(user_id)
    database.execute(f'''
        INSERT INTO Process ( 
            user_id, 
            start_time, 
            end_time, 
            quantity_split,
            silence_ranges,
            get_audio_done, 
            split_audio_done, 
            transcript_done, 
            create_audio_done, 
            unify_audio_done,
            last_update,
            relative_path,
            img,
            source_lang,
            target_lang,
            original_file_name 
        ) VALUES (
            "{user_id}",
            "{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}",
            "{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}",
            0,
            "",
            "0%",
            "0%",
            "0%",
            "0%",
            "0%",
            "{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}",
            "{relative_path}",
            "{relative_path}/tumbnail.jpg",
            "{source_lang}",
            "{target_lang}",
            "{original_file_name}"
            )
    ''')
    return get_last_process()

def get_process_by_id(process_id):
    rows = database.select("Process", columns=[], condition=f"process_id = {process_id}")
    return Process(*rows[0])

def get_process_by_user_id(user_id):
    rows = database.select("Process", columns=[], condition=f"user_id = {user_id}")
    process_dictionary = []
    if len(rows) == 0:
        return []
    process_list = [Process(*row) for row in rows]
    for p in process_list:
        process_dictionary.append(p.__dict__)
    return process_dictionary

def get_process_by_relative_path(relative_path):
    rows = database.select("Process", columns=[], condition=f"relative_path = {relative_path}")
    return Process(*rows[0])

def get_all_process():
    return database.select("Process")

def get_last_process():
    process = database.select("Process")
    return Process(*process[len(process)-1])

def update_process(process):
    database.update("Process", data=process, condition=f"process_id = {process['process_id']}")

def update_process_by_relative_path(process):
    database.update("Process", data=process, condition=f"relative_path = '{process['relative_path']}'")

if __name__ == '__main__':
    main()
