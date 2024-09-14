from flask import Flask, jsonify, request, send_file, abort
import os
from config import PATH_RELATIVE
from flasgger import Swagger
from utils_loger import log_info
from utils_voice_generator import initialize_tts_model
from main import main
from datetime import datetime

app = Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "API de tradução de videos",
        "description": "Documentação da API de tradução de videos",
        "version": "0.0.1"
    }
})

tts_model = initialize_tts_model()

log_info("API running")

@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Service working!"})

# @app.route('/api/data', methods=['POST'])
# def get_data():
#     data = request.get_json()
#     return jsonify({"received_data": data})

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint para upload de arquivos .mp4 com dados JSON
    ---
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
      - name: user
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
    user = request.form.get('user')

    if not source_language or not dest_language or not user:
        return jsonify({"error": "Missing required form data"}), 400

    # Valida o tipo de arquivo
    if file and file.filename.endswith('.mp4'):
      relative_path = os.path.join(PATH_RELATIVE, user, datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
      if not os.path.exists(relative_path):
        os.makedirs(relative_path)

      file_path = os.path.join(relative_path, file.filename)
      file.save(file_path)

      main(file_path, source_language, dest_language, relative_path, tts_model)

      return jsonify({
          "message": "File uploaded successfully!",
          "source_language": source_language,
          "dest_language": dest_language,
          "user": user,
          "url_result_file": os.path.join(relative_path, "result.mp4")
      }), 200 
    else:
        return jsonify({"error": "Only .mp4 files are allowed"}), 400

@app.route('/download', methods=['GET'])
def download_file():
  """
  File download endpoint
  ---
  parameters:
    - name: file_path
      in: query
      type: string
      required: true
      description: Path of the file to download
  responses:
    200:
      description: File downloaded successfully
    404:
      description: File not found
  """
  file_path = request.args.get('file_path')

  if not os.path.isfile(file_path):
      abort(404, description="File not found")

  return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)