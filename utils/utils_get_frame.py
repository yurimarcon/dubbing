import os


def get_frame(video_path, file_name="frame_1.jpg"):
    os.system(
        f"ffmpeg -i {video_path} -vf 'select=eq(n\,100)' -vframes 1 {file_name})"
            )
