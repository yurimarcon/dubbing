import os
import subprocess


def get_frame(video_path, file_name):
    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,                  # Caminho do vídeo
        "-vf", "select=eq(n\\,100)",       # Selecionar o quadro 100 (\\ para escapar a vírgula)
        "-vframes", "1",                   # Extrair apenas um frame
        file_name                          # Caminho para salvar o arquivo de saída
    ]
    subprocess.run(command, check=True)
