import os
from config import SOURCE_FOLDER
from datetime import datetime

LOG_FILE_NAME = "log.txt"
LOG_PATH = f"{SOURCE_FOLDER}{LOG_FILE_NAME}"

def write_log(text, typeLog):
    try:
        # Abre o arquivo no modo de anexar (append)
        with open(LOG_PATH, "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            log_file.write(f"[{timestamp}][{typeLog}]: {text}\n")
    except Exception as e:
        print(f"=========>>> Error writing to log file: {e}")

def log_info(text):
    write_log(text, "INFO")

def log_warning(text):
    print(f"=========>>> WARNING: {text}")
    write_log(text, "WARNING")

def log_error(text):
    print(f"=========>>> ERROR: {text}")
    write_log(text, "ERROR")

if __name__ == "__main__":
    main()