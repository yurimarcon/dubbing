import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('dubbing-process')

def update_field_string_repository(pk, sk, field, value):
    print("====>>>>",field, value )

    current_time = datetime.utcnow().isoformat()
    if isinstance(value, float):
        value = Decimal(value)

    if isinstance(value, list) and all(isinstance(item, tuple) for item in value):
        value = f"{value}"

    try:
        response = table.update_item(
            Key={
                'PK': pk,
                'SK': sk
            },
            UpdateExpression=f"SET #{field} = :{field}, #last_update = :last_update",
            ExpressionAttributeValues={
                f":{field}": value,
                ":last_update": current_time
            },
            ExpressionAttributeNames={
                f"#{field}": field,
                "#last_update": "last_update"
            },
            ReturnValues="UPDATED_NEW"  # Retorna os valores atualizados
        )
        return response

    except ClientError as e:
        print(f"Erro ao atualizar item: {e.response['Error']['Message']}")
        return None

# update_field_string_repository(
#     "process-dubbing-video-fece7527-a738-4ac9-90f9-2bb6f3b7bbba",
#     "admin 3",
#     "transcript_audio_done",
#     "100%"
# )