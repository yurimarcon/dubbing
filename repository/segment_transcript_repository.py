from  sqlite4  import  SQLite4
from entities.segment import Segment
from datetime import datetime

database = SQLite4("database.db")

database.connect()

def create_segment(
        segment_id,
        transcript_id, 
        process_id, 
        user_id, 
        text, 
        start, 
        end
        ):
    database.execute(f'''
        INSERT INTO Segments_transcript( 
            segment_id,
            transcript_id, 
            process_id, 
            user_id, 
            text, 
            start, 
            end
        ) VALUES (
            "{segment_id}",
            "{transcript_id}",
            "{process_id}",
            "{user_id}",
            "{text}",
            "{start}",
            "{end}"
            )
    ''')

def get_segment(segment_id):
    rows = database.select("Segments_transcript", columns=[], condition=f"segment_id = {segment_id}")
    return Segment(*rows[0])

def get_all_segments():
    return database.select("Segments_transcript")

def update_segment(segment):
    database.update("Segments_transcript", data=segment, condition=f"segment_id = {segment['segment_id']}")

if __name__ == '__main__':
    main()
