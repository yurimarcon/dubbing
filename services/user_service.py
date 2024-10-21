import sys, os
import decimal
from pydub import AudioSegment
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from repository.users_repository import create_user, update_user, get_user_by_id
from repository.dynamo_user_repository import get_user_dynamo_by_id, update_user_field_repository

def create_new_user(name, email, tel, password):
    create_user(name, email, tel, password, 10, 0)

def activate_user(user_id):
    user = get_user_by_id(user_id)
    user_to_update = {
        "user_id": user.user_id,
        "is_active": 1
    }
    update_user(user_to_update)

def deactivate_user(user_id):
    user = get_user_by_id(user_id)
    user_to_update = {
        "user_id": user.user_id,
        "is_active": 0
    }
    update_user(user_to_update)

def get_user_by_id_service(user_id):
    return get_user_by_id(user_id)

def verify_plan_free_limit(user_id, original_audio_path):
    
    user = get_user_dynamo_by_id(user_id)
    response_validation = ""
    limit_free_seconds = 600

    # Verify if user exeded free limit
    atual_audio = AudioSegment.from_file(original_audio_path)
    future_duration = user['seconds_processed_in_month'] + decimal.Decimal(len(atual_audio)/1000)
    print(user)

    if user['is_payer'] == True or future_duration <= limit_free_seconds:
        update_user_field_repository(
            user['PK'],
            user['SK'],
            'seconds_processed_in_month',
            future_duration.quantize(decimal.Decimal('0.001')) # Define 3 casas decimais
        )
        current_time = datetime.utcnow().isoformat()
        update_user_field_repository(
            user['PK'],
            user['SK'],
            'last_process_date',
            current_time
        )
    else:
        response_validation = "Exceded limit";
        print(response_validation)

    return response_validation
