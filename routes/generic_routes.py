from flask import Blueprint, jsonify
from utils.utils_loger import log_info

generic_bp = Blueprint('generic', __name__)

@generic_bp.route('/verify', methods=['GET'])
def home():
    """
    Verify service working.
    ---
    tags:
        - Verify API
    responses:
        200:
            description: Service Working!
    """
    log_info("Verify service working.")
    return jsonify({"message": "Service working!"})
