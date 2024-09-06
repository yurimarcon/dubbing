import os
from pydub import AudioSegment
from pydub.silence import detect_silence
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
from utils_audio import extract_audio_from_video, detect_silences, create_silence
from config import SILENCE_NAME, SPLITED_INITIAL_AUDIO_NAME

def cut_video_at_silence(audio_path, silence_intervals, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_duration = AudioSegment.from_file(audio_path).duration_seconds
    start_time = 0

    for idx, (silence_start, silence_end) in enumerate(silence_intervals):
        create_silence(silence_start, silence_end, f"{output_folder}{SILENCE_NAME}{idx}.wav")
        if silence_end == round(video_duration, 3):
            break

        if silence_start == 0:
            start_time = silence_end
           
        if idx + 1 < len(silence_intervals):
            next_start_sil, next_finish_sil = silence_intervals[idx + 1]
        else:
            next_start_sil = None
            next_finish_sil = None
        print(next_start_sil, next_finish_sil)
        end_time = next_start_sil

        output_file = f"{output_folder}{SPLITED_INITIAL_AUDIO_NAME}{idx}.wav"
        ffmpeg_tools.ffmpeg_extract_subclip(audio_path, start_time, end_time, targetname=output_file)
        start_time = next_finish_sil
