from  sqlite4  import  SQLite4
from entities.process import Process
from datetime import datetime

database = SQLite4("database.db")

database.connect()

def create_process(
        user_id, 
        start_time,
        end_time,
        get_audio_done, 
        split_audio_done,
        transcript_done, 
        create_audio_done, 
        unify_audio_done
    ):
    database.execute(f'''
        INSERT INTO Process ( 
            user_id, 
            start_time, 
            end_time, 
            get_audio_done, 
            split_audio_done, 
            transcript_done, 
            create_audio_done, 
            unify_audio_done
        ) VALUES (
            "{user_id}",
            "{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}",
            "{end_time}",
            "{get_audio_done}",
            "{split_audio_done}",
            "{transcript_done}",
            "{create_audio_done}",
            "{unify_audio_done}"
            )
    ''')

def get_process(process_id):
    rows = database.select("Process", columns=[], condition=f"process_id = {process_id}")
    return Process(*rows[0])

def get_all_process():
    return database.select("Process")

def update_process(process):
    database.update("Process", data=process, condition=f"process_id = {process['process_id']}")

if __name__ == '__main__':
    main()
