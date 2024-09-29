import boto3
import sys
from config import BUCKET_NAME, BUCKET_URL

def download_file_from_s3(bucket_name, object_key, file_name):
    # Cria o cliente S3
    s3 = boto3.client('s3')

    try:
        # Faz o download do arquivo
        s3.download_file(bucket_name, object_key, file_name)
        print(f'{file_name} downloaded successfully from {bucket_name}/{object_key}')
    except Exception as e:
        print(f"Error downloading the file: {e}")



def main(bucket_name, object_key, file_name):
    download_file_from_s3(bucket_name, object_key, file_name)

if __name__ == '__main__':

    # bucket_name = 'dubbing-videos'
    # object_key = 'admin/27-09-2024-15:01:36/t.mp4'  # Caminho do vídeo no bucket S3
    # file_name = 'result/video_baixado.mp4'  # Nome com o qual o vídeo será salvo localmente
    
    bucket_name = sys.argv[0]
    object_key = sys.argv[1]
    file_name = sys.argv[2]
    
    main()