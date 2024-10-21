import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from decimal import Decimal
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('dubbing-users')

def get_user_dynamo_by_id(user_id):
    response = table.scan(
        FilterExpression=Attr('user_id').eq(user_id)
    )
    return response['Items'][0]

def update_user_field_repository(pk, sk, field, value):
    print("dubbing-users ====>>>>",field, value )

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
            UpdateExpression=f"SET #{field} = :{field}, #last_updated = :last_updated",
            ExpressionAttributeValues={
                f":{field}": value,
                ":last_updated": current_time
            },
            ExpressionAttributeNames={
                f"#{field}": field,
                "#last_updated": "last_updated"
            },
            ReturnValues="UPDATED_NEW"  # Retorna os valores atualizados
        )
        return response

    except ClientError as e:
        print(f"Erro ao atualizar item: {e.response['Error']['Message']}")
        return None

