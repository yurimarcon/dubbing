from flask import Flask, jsonify, request
import os
from config import SOURCE_FOLDER
from flasgger import Swagger
from celery import Celery
from utils_loger import log_info

app = Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "API de tradução de videos",
        "description": "Documentação da API de tradução de videos",
        "version": "0.0.1"
    }
})

app.config['SOURCE_FOLDER'] = SOURCE_FOLDER

# Configuração do Celery
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Certifique-se de que o diretório existe
if not os.path.exists(SOURCE_FOLDER):
    os.makedirs(SOURCE_FOLDER)

log_info("API running")

@celery.task(bind=True)
def long_task(self, file_path):
    log_info("Prepare to send task...")
    os.system(f"python main.py {file_path}")
    return "=====>>> long_task conclude!"

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
    Endpoint para upload de arquivos .mp4
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: O arquivo .mp4 para upload
    responses:
      200:
        description: Upload bem-sucedido
    """
    log_info("Request recived...")
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.mp4'):
        file_path = os.path.join(app.config['SOURCE_FOLDER'], file.filename)
        file.save(file_path)
        process_id = long_task.apply_async(args=[file_path])  # Correção aqui
        return jsonify({"message": f"File uploaded successfully to {file_path}, process ID: {process_id}"}), 200
    else:
        return jsonify({"error": "Only .mp4 files are allowed"}), 400

@app.route('/task-status/<task_id>', methods=['GET'])
def task_status(task_id):
    """
    Endpoint para consultar o status de uma tarefa
    ---
    parameters:
      - name: task_id
        in: path
        type: string
        required: true
        description: ID da tarefa para consultar o status
    responses:
      200:
        description: Status da tarefa consultado com sucesso
        schema:
          type: object
          properties:
            state:
              type: string
              description: O estado atual da tarefa
            status:
              type: string
              description: Status adicional da tarefa, aplicável em caso de erro
            result:
              type: string
              description: Resultado da tarefa, aplicável se a tarefa for bem-sucedida
      404:
        description: Tarefa não encontrada
    """
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {"state": task.state, "status": "Aguardando..."}
    elif task.state != 'FAILURE':
        response = {"state": task.state, "result": task.result}
    else:
        response = {"state": task.state, "status": str(task.info)}  # task.info tem a exceção em caso de falha
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)