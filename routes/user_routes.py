from flask import Blueprint, jsonify, request
from utils.utils_loger import log_info
from services.user_service import create_new_user, activate_user, deactivate_user, get_user_by_id_service

user_bp = Blueprint('user', __name__)

@user_bp.route('/create_user', methods=['POST'])
def create_user():
    """
    Create User
    ---
    tags:
        - User
    parameters:
        - name: user_name
          in: body
          type: string
          required: true
          description: User Name
        - name: user_email
          in: body
          type: string
          required: true
          description: User e-mail
        - name: user_tel
          in: body
          type: string
          required: true
          description: User Telephone
        - name: user_password
          in: body
          type: string
          required: true
          description: User password
    responses:
        200:
            description: Create User
    """
    log_info("Create User.")
    name = request.body.get('user_name')
    email = request.body.get('user_email')
    tel = request.body.get('user_tel')
    password = request.body.get('user_password')
    user = create_new_user(name, email, tel, password)
    return jsonify({"message": "User created with success!"})

@user_bp.route('/activate_user', methods=['PUT'])
def activate_user_endpoint():
    """
    Activate User
    ---
    tags:
        - User
    parameters:
        - name: user_id
          in: query
          type: integer
          required: true
          description: User Id
    responses:
        200:
            description: Activate User
    """
    log_info("Create User.")
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    is_cativated = activate_user(user_id)
    return jsonify({"message": "User activated with success!"})

@user_bp.route('/deactivate_user', methods=['PUT'])
def deactivate_user_endpoint():
    """
    Deactivate User
    ---
    tags:
        - User
    parameters:
        - name: user_id
          in: query
          type: integer
          required: true
          description: User Id
    responses:
        200:
            description: Deactivate User
    """
    log_info("Deactivate User.")
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    is_cativated = deactivate_user(user_id)
    return jsonify({"message": "User deactivated with success!"})

@user_bp.route('/get-user-by-id', methods=['GET'])
def get_user_by_id_endpoint():
    """
    Get User by Id
    ---
    tags:
        - User
    parameters:
        - name: user_id
          in: query
          type: integer
          required: true
          description: User Id
    responses:
        200:
            description: Get User by id
    """
    log_info("Get User by id.")
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    user = get_user_by_id_service(user_id)
    return jsonify(user.__dict__), 200
