from worker import receive_messages
from download_video import download_file_from_s3
from config import BUCKET_NAME

def main():
    message = receive_messages()
    print(message['original_file_path'])

    if message['original_file_path'] is not None: 
        download_file_from_s3(
            BUCKET_NAME, 
            message['original_file_path'], 
            'result/v.mp4'
        )

if __name__ == '__main__':
    main()