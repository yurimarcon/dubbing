from flask import Flask, jsonify, request, send_file, abort
import os
from flasgger import Swagger
from utils.utils_loger import log_info
from datetime import datetime
from routes.upload_routes import upload_bp
from routes.download_routes import download_bp
from routes.generic_routes import generic_bp

app = Flask(__name__)

swagger = Swagger(app, template={
    "info": {
        "title": "API de tradução de videos",
        "description": "Documentação da API de tradução de videos",
        "version": "0.0.1"
    }
})

log_info("API running")

app.register_blueprint(upload_bp)
app.register_blueprint(download_bp)
app.register_blueprint(generic_bp)

if __name__ == '__main__':
    app.run(debug=True)