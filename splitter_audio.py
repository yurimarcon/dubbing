import os
from pydub import AudioSegment
from pydub.silence import detect_silence
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
from utils_audio import extract_audio_from_video, detect_silences
from config import SILENCE_NAME, SPLITED_INITIAL_AUDIO_NAME

def cut_video_at_silence(audio_path, silence_intervals, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_duration = AudioSegment.from_file(audio_path).duration_seconds
    start_time = 0
    quantity_sliced_audios = 0
    next_start_sil = video_duration
    next_finish_sil = None
    output_file = f"{output_folder}{SPLITED_INITIAL_AUDIO_NAME}"

    for idx, (silence_start, silence_end) in enumerate(silence_intervals):
        
        # if is the last silence and not is a unique silence
        if silence_end == round(video_duration) and len(silence_intervals) > 1:
            break

        # if is the first silence and this silence is in start
        if silence_start == 0:
            start_time = silence_end
        
        # if has just one silence interval
        if len(silence_intervals) == 1 and silence_start != 0:
            end_time = silence_start
            ffmpeg_tools.ffmpeg_extract_subclip(
                audio_path, 
                start_time, 
                end_time, 
                targetname=f"{output_file}{quantity_sliced_audios}.wav")
            quantity_sliced_audios+=1 # it fix file name in second part audio

            # if has just one silence interval and this silence is in the end
            if silence_end == round(video_duration):
                break

            start_time = silence_end
            end_time = video_duration
        
        # if has just one silence and it is in start audio
        elif len(silence_intervals) == 1 and silence_start == 0:
            start_time = silence_end
            end_time = video_duration

        # if not is last silence interval
        elif idx + 1 < len(silence_intervals):
            next_start_sil, next_finish_sil = silence_intervals[idx + 1]
            end_time = next_start_sil

        # if is last silence interval
        else:
            end_time = next_start_sil

        ffmpeg_tools.ffmpeg_extract_subclip(
                audio_path, 
                start_time, 
                end_time, 
                targetname=f"{output_file}{quantity_sliced_audios}.wav")
        start_time = next_finish_sil
        quantity_sliced_audios+=1
    
    return quantity_sliced_audios
