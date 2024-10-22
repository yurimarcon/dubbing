import os
import subprocess
import sys
from utils.utils_url_parser import validate_url

def download_from_youtube(target_file_path, url_yt):

    if os.path.exists(target_file_path):
        print(f"Do not need youtube download. {target_file_path}")
        return
    
    url_validated = validate_input(url_yt)

    command = [
        "yt-dlp", 
        "-o", 
        target_file_path,
        url_validated
    ]
    subprocess.run(command, check=True)

    if not os.path.exists(target_file_path):
        path_relative = os.path.dirname(target_file_path)
        files = os.listdir(path_relative)
        video_downloaded = os.path.join(path_relative,files[0])
        convert_video_to_mp4(video_downloaded, target_file_path)

def convert_video_to_mp4(path_file_to_convert, path_file_converted):
    command = [
        "ffmpeg",
        "-i",
        path_file_to_convert,
        path_file_converted
    ]
    subprocess.run(command, check=True) 
    os.remove(path_file_to_convert)

def main():
    pass

if __name__ == "__main__":
    main()