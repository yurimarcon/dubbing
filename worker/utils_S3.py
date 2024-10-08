import boto3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import BUCKET_NAME, BUCKET_URL

def upload_video_to_s3(local_file_path, s3_file_path=None):
    # Se object_name não for especificado, o nome do arquivo será usado
    if s3_file_path is None:
        s3_file_path = local_file_path

    # Inicialize o cliente S3
    s3_client = boto3.client('s3')

    try:
        # Faça o upload do arquivo
        s3_client.upload_file(local_file_path, BUCKET_NAME, s3_file_path)
        print(f"Upload do arquivo {local_file_path} para o bucket {BUCKET_NAME} concluído com sucesso.")
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except NoCredentialsError:
        print("Credenciais não disponíveis.")

def download_file_from_s3(bucket_name, object_key, local_file_path):
    print(bucket_name, object_key, local_file_path)

    if os.path.exists(local_file_path):
        return

    # Cria o cliente S3
    s3 = boto3.client('s3')

    try:
        # Create directory where will dowload the video.
        os.makedirs(os.path.dirname(local_file_path))
        # make download file
        s3.download_file(bucket_name, object_key, local_file_path)
        print(f'{local_file_path} downloaded successfully from {bucket_name}/{object_key}')

        temp_file_name, file_extension = os.path.splitext(local_file_path)
        if file_extension == ".mov":
            command = [
                "ffmpeg",
                "-i",
                local_file_path,
                f"{temp_file_name}.mp4"
            ]
            subprocess.run(command, check=True)
            os.remove(local_file_path)

    except Exception as e:
        print(f"Error downloading the file: {e}")

def main(bucket_name, object_key, file_name):
    download_file_from_s3(bucket_name, object_key, file_name)

if __name__ == '__main__':

    # bucket_name = 'dubbing-videos'
    # object_key = 'admin/27-09-2024-15:01:36/t.mp4'  # Caminho do vídeo no bucket S3
    # file_name = 'result/video_baixado.mp4'  # Nome com o qual o vídeo será salvo localmente
    
    S3_file_path = sys.argv[1]
    local_file_path = sys.argv[2]
    
    # main(bucket_name, S3_file_path, local_file_path)

    upload_video_to_s3(local_file_path, S3_file_path)