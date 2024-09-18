from  sqlite4  import  SQLite4

database = SQLite4("database.db")
database.connect()

def create_table_user():
    database.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            tel TEXT NOT NULL,
            password TEXT NOT NULL,
            credits INTEGER NOT NULL,
            is_active INTEGER NOT NULL,
            created_date TEXT NOT NULL,
            last_update TEXT NOT NULL
        )
    ''')

def create_table_process():
    database.execute('''
        CREATE TABLE IF NOT EXISTS Process (
            process_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            start_time TEXT,
            end_time TEXT,
            quantity_split INTEGER,
            silence_ranges TEXT,
            get_audio_done TEXT,
            split_audio_done TEXT,
            transcript_done TEXT,
            create_audio_done TEXT,
            unify_audio_done TEXT,
            last_update TEXT,
            relative_path TEXT,
            download_file_name TEXT
        )
    ''')

def create_table_transcripts():
    database.execute('''
        CREATE TABLE IF NOT EXISTS Transcript (
            transcript_id INTEGER PRIMARY KEY AUTOINCREMENT,
            process_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL
        )
    ''')

def create_table_segments():
    database.execute('''
        CREATE TABLE IF NOT EXISTS Segments_transcript(
            segment_id INTEGER NOT NULL,
            transcript_id INTEGER NOT NULL,
            process_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            start REAL NOT NULL,
            end REAL NOT NULL
        )
    ''')

def create_all_tables():
    create_table_user()
    create_table_process()
    create_table_transcripts()
    create_table_segments()

if __name__ == "__main__":
    main()
