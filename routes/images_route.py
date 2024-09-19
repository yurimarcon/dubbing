from flask import Blueprint, send_from_directory
import os
from utils.utils_loger import log_info

images_bp = Blueprint('images', __name__)

@images_bp.route('/result/<path:filename>')
def serve_image(filename):
    directory = os.path.join(images_bp.root_path, '../result/')
    print(directory)
    return send_from_directory(directory, filename)