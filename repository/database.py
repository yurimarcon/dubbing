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
            is_active INTEGER NOT NULL
        )
    ''')

def create_table_process():
    database.execute('''
        CREATE TABLE IF NOT EXISTS Process (
            process_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            get_audio_done INTEGER NOT NULL,
            split_audio_done INTEGER NOT NULL,
            transcript_done INTEGER NOT NULL,
            create_audio_done INTEGER NOT NULL,
            unify_audio_done INTEGER NOT NULL
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
        CREATE TABLE IF NOT EXISTS Segments (
            segment_id INTEGER NOT NULL,
            transcript_id INTEGER NOT NULL,
            process_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            start REAL NOT NULL,
            end REAL NOT NULL
        )
    ''')

if __name__ == "__main__":
    main()
