import boto3
import json
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import BUCKET_URL

# Criando o cliente SQS
sqs = boto3.client('sqs', region_name='us-east-1')  # Altere para a região correta

# URL da sua fila SQS
# queue_url = 'https://sqs.us-east-1.amazonaws.com/093711393814/dubbing-sqs'
queue_url = BUCKET_URL

def receive_messages():
    try:
        # Recebe uma ou mais mensagens da fila
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,  # Quantidade máxima de mensagens a receber
            WaitTimeSeconds=10,      # Long polling para aguardar mensagens
            VisibilityTimeout=30     # Tempo que a mensagem fica invisível após leitura
        )
        
        # Verifica se recebeu mensagens
        if 'Messages' in response:
            for message in response['Messages']:
                return message['ReceiptHandle'], json.loads(message['Body'])
        else:
            print("Nenhuma mensagem na fila.")
            return None, None

    except Exception as e:
        print(f"Erro ao receber mensagens: {e}")

def remove_message_from_queue(receiptHandle):
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receiptHandle
    )
    print("Mensagem deletada com sucesso.")
