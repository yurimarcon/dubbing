from flask import Blueprint, jsonify, request
from utils.utils_loger import log_info
from services.process_service import get_process_by_id, get_process_by_user_id_service

process_bp = Blueprint('process', __name__)

@process_bp.route('/process-by-id', methods=['GET'])
def home():
    """
    Verify service working.
    ---
    tags:
        - Process
    parameters:
        - name: process_id
          in: query
          type: integer
          required: true
          description: Process ID
    responses:
        200:
            description: Service Working!
    """
    process_id = request.args.get('process_id')
    process = get_process_by_id(process_id)    
    return jsonify(process.__dict__), 200

@process_bp.route('/process-by-user', methods=['GET'])
def get_process_by_user():
    """
    Verify service working.
    ---
    tags:
        - Process
    parameters:
        - name: user_id
          in: query
          type: integer
          required: true
          description: User ID
    responses:
        200:
            description: Get process by usr id
    """
    user_id = request.args.get('user_id')
    process= get_process_by_user_id_service(user_id)
    print(process)
    return jsonify(process), 200
