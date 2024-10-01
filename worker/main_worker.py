import sys, os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import BUCKET_NAME
from main import main as main_command_line
from utils.utils_voice_generator import initialize_tts_model
from worker.sqs_consumer import receive_messages, remove_message_from_queue
from worker.utils_S3 import download_file_from_s3, upload_video_to_s3

tts_model = initialize_tts_model()

def get_message_sqs_and_process():
    receiptHandle, message = receive_messages()

    if message != None: 
        s3_path_file = message['original_file_path']
        source_lang = message['source_lang']
        target_lang = message['target_lang']
        local_original_video_path = os.path.join("result/", s3_path_file)
        relative_path = os.path.dirname(local_original_video_path)
        user_id = 1
        
        download_file_from_s3(BUCKET_NAME, s3_path_file, local_original_video_path)    
        main_command_line(local_original_video_path, source_lang, target_lang, relative_path, tts_model, user_id, message)

        s3_result_file_path = os.path.join(os.path.dirname(s3_path_file), "result.mp4")
        upload_video_to_s3(os.path.join(relative_path, "result.mp4"), s3_result_file_path)
        remove_message_from_queue(receiptHandle)

def main():
    while True:
        print("Going to verify sqs...")
        get_message_sqs_and_process()
        time.sleep(60)

if __name__ == '__main__':
    main()