from flask import Blueprint, jsonify, request
import os
from config import PATH_RELATIVE
from main import main
from utils.utils_loger import log_info
from utils.utils_voice_generator import initialize_tts_model
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from repository.users_repository import get_user_by_name

tts_model = initialize_tts_model()
executor = ThreadPoolExecutor(max_workers=2)
upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint para upload de arquivos .mp4 com dados JSON
    ---
    tags:
      - Core
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: O arquivo .mp4 para upload
      - name: source_language
        in: formData
        type: string
        required: true
        description: A linguagem de origem do arquivo
      - name: dest_language
        in: formData
        type: string
        required: true
        description: A linguagem de destino para tradução
      - name: user_name
        in: formData
        type: string
        required: true
        description: O usuário que está enviando a requisição
    responses:
      200:
        description: Upload bem-sucedido
    """
    log_info("Request received...")

    # Verifica se o arquivo está presente na requisição
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Verifica se os dados de linguagem e usuário estão presentes
    source_language = request.form.get('source_language')
    dest_language = request.form.get('dest_language')
    user_name = request.form.get('user_name')

    if not source_language or not dest_language or not user_name:
        return jsonify({"error": "Missing required form data"}), 400

    user = get_user_by_name(user_name)
    print(user)
    if not user:
      return jsonify({"error": "User do not registred"}), 400

    # Valida o tipo de arquivo
    if file and file.filename.endswith('.mp4'):
        relative_path = os.path.join(PATH_RELATIVE, user.name, datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        if not os.path.exists(relative_path):
            os.makedirs(relative_path)

        file_path = os.path.join(relative_path, file.filename)
        file.save(file_path)

        executor.submit(main, file_path, source_language, dest_language, relative_path, tts_model, user.user_id)

        return jsonify({
            "message": "File uploaded successfully!",
            "source_language": source_language,
            "dest_language": dest_language,
            "user": user.name,
            "sequence": user.user_id
        }), 200 
    else:
        return jsonify({"error": "Only .mp4 files are allowed"}), 400
