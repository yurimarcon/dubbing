from  sqlite4  import  SQLite4
from entities.transcript import Transcript
from datetime import datetime

database = SQLite4("database.db")

database.connect()

def create_transcript(
        transcipt_id,
        process_id,
        user_id
        ):
    database.execute(f'''
        INSERT INTO Transcript ( 
            transcript_id,
            process_id,
            user_id
        ) VALUES (
            "{transcipt_id}",
            "{process_id}",
            "{user_id}"
            )
    ''')

def get_transcript(transcript_id):
    rows = database.select("Transcript", columns=[], condition=f"transcript_id = {transcript_id}")
    return Transcript(*rows[0])

def get_all_transcript():
    return database.select("Transcript")

def update_transcript(transcript):
    database.update("Transcript", data=transcript, condition=f"transcript_id = {transcript['transcript_id']}")

if __name__ == '__main__':
    main()
