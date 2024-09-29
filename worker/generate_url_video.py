import boto3
from botocore.exceptions import NoCredentialsError

def generate_presigned_url(bucket_name, object_name, expiration=3600):
    """Gerar URL pré-assinada para o vídeo no S3"""
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_name
            },
            ExpiresIn=expiration
        )
    except NoCredentialsError:
        return None
    return response

# Exemplo de uso
bucket_name = 'dubbing-videos'
# object_name = 'admin/27-09-2024-15:01:36/t.mp4'
object_name = 'admin/28-09-2024-12:47:04/74922038739__E7E7AA3D-30DB-4E7A-ABC6-A73C43FA2557.MOV'
seconds_to_expiration = 3600
url = generate_presigned_url(bucket_name, object_name, seconds_to_expiration)
print(f"URL do vídeo: {url}")
