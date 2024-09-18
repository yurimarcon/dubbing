from repository.users_repository import create_user, update_user, get_user_by_id

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
