import boto3
import json

# Criando o cliente SQS
sqs = boto3.client('sqs', region_name='us-east-1')  # Altere para a região correta

# URL da sua fila SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/093711393814/dubbing-sqs'

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
                # print(f"Mensagem recebida: {message['Body']}")
                
                # Processar a mensagem aqui (exemplo: fazer algo com o conteúdo JSON)
                # data = json.loads(message['Body'])
                # print(f"Dados da mensagem: {data}")
                return json.loads(message['Body'])

                # Após processar a mensagem, você pode deletá-la da fila
                # sqs.delete_message(
                #     QueueUrl=queue_url,
                #     ReceiptHandle=message['ReceiptHandle']
                # )
                # print("Mensagem deletada com sucesso.")
        else:
            print("Nenhuma mensagem na fila.")

    except Exception as e:
        print(f"Erro ao receber mensagens: {e}")

# Chamando a função para receber mensagens
# receive_messages()
