import os
import subprocess
import sys

def download_from_youtube(target_file_path, url_yt):
    command = [
        "yt-dlp", 
        "-o", 
        target_file_path,
        url_yt
    ]
    subprocess.run(command, check=True)
    convert_video_to_mp4(target_file_path+".webm", target_file_path)

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