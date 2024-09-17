from flask import Blueprint, request, send_file, abort
import os
from utils.utils_loger import log_info

download_bp = Blueprint('download', __name__)

@download_bp.route('/download', methods=['GET'])
def download_file():
  """
  File download endpoint
  ---
  tags:
    - Core
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
