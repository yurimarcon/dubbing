from pydub import AudioSegment
from pydub.silence import detect_silence
import os
from utils_loger import log_info
from config import PATH_RELATIVE

def load_audio(file_path):
    with open(file_path, 'rb') as f:
        audio = AudioSegment.from_file(f)
    return audio

def get_silence_ranges (inputAudio):
    original_audio = AudioSegment.from_file(inputAudio)
    return detect_silence(original_audio, min_silence_len=1000, silence_thresh=-35)

def detect_silences(audio_path):
    audio = AudioSegment.from_file(audio_path)
    silences = detect_silence(audio, min_silence_len=600, silence_thresh=-44)
    return [(start / 1000, stop / 1000) for start, stop in silences]  # Convert to seconds
    
def create_silence(silence_start, silence_end, path_audio_file):
    duration_silence = (silence_end - silence_start) * 1000
    print("duration_silence: ", duration_silence)
    silence = AudioSegment.silent(duration=duration_silence)
    silence.export(path_audio_file, format="wav")

def get_initial_silence_duration (silence_ranges):
    return silence_ranges[0][1] if silence_ranges and silence_ranges[0][0] == 0 else 0

def calculate_speed_factory(duratio_audio_base, duratio_audio_spected):
    if duratio_audio_base == 0 or duratio_audio_spected == 0:
        # if any duration did 0 do not calculate nothing
        return 1
    speed_factor = duratio_audio_base / duratio_audio_spected
    log_info(f"Real speed_factory: {speed_factor}")
    if speed_factor < 0.9:
        speed_factor = 0.9
    elif speed_factor > 1.8:
        speed_factor = 1.8
    return speed_factor

def get_speed_factory (segment_by_transcript, file_path_to_verify):
    audio = AudioSegment.from_file(file_path_to_verify)
    duration_segment = len(audio) / 1000  # Converting to miliseconds
    duration_transcipt = segment_by_transcript['end'] - segment_by_transcript['start']
    return calculate_speed_factory(duration_segment, duration_transcipt)
    
def adjust_segment_speed(segment, initial_file, adjusted_file):
    speed_factor = get_speed_factory(segment, initial_file)
    print("===============================")
    print(f'ffmpeg -i {initial_file} -filter:a "atempo={speed_factor}" {adjusted_file}')
    print("===============================")
    os.system(f'ffmpeg -i {initial_file} -filter:a "atempo={speed_factor}" {adjusted_file}')

def ajust_speed_audio(audio_without_ajust, audio_time_expected, path_new_audio):
    file_audio_without_ajust = AudioSegment.from_file(audio_without_ajust)
    duration_audio_without_ajust = len(file_audio_without_ajust)
    file_audio_time_expected = AudioSegment.from_file(audio_time_expected)
    duration_audio_time_expected = len(file_audio_time_expected)

    speed_factor = calculate_speed_factory(duration_audio_without_ajust, duration_audio_time_expected)
    
    os.system(f'ffmpeg -i {audio_without_ajust} -filter:a "atempo={speed_factor}" {path_new_audio}')
    # ajust_time_video_puting_silence_in_start(path_new_audio, audio_time_expected)
    
    # Record log with name and time duration sniped audio
    audio_generated = AudioSegment.from_file(f"{path_new_audio}")
    log_info(f"{path_new_audio} {len(audio_generated)}")

    return speed_factor

def remove_silence_unecessery(audio_path):
    audio_did_ajusted = AudioSegment.from_file(audio_path)
    silence_ranges = detect_silence(audio_did_ajusted, min_silence_len=2000, silence_thresh=-35)
    if not silence_ranges:
        return
    print("silence_ranges =========>>>>>>>> ", silence_ranges)
    for silence in silence_ranges:
        before_silence = audio_did_ajusted[:silence[0]]
        after_silence = audio_did_ajusted[silence[1]:]
        audio_without_silence = before_silence + after_silence
        audio_without_silence.export(audio_path, format="wav")

def ajust_time_video_puting_silence_in_start (file_path_to_ajust, path_original_audio):
    audio_did_ajusted = AudioSegment.from_file(file_path_to_ajust)
    duration_audio_did_ajusted = len(audio_did_ajusted) / 1000
    original_audio = AudioSegment.from_file(path_original_audio)
    duration_original_audio = len(original_audio)
    duration_silence = (duration_original_audio - duration_audio_did_ajusted) * 1000
    silence = AudioSegment.silent(duration=duration_silence)
    silence += audio_did_ajusted
    silence.export(file_path_to_ajust, format="wav")

def put_silence_to_ajust_time (segment, file_path_to_ajust):
    audio_did_ajusted = AudioSegment.from_file(file_path_to_ajust)
    duration_audio_did_ajusted = len(audio_did_ajusted) / 1000
    duration_transcipt = segment['end'] - segment['start']
    print(f"{duration_audio_did_ajusted} > {duration_transcipt}")
    if duration_audio_did_ajusted < duration_transcipt:
        time_less = (duration_transcipt - duration_audio_did_ajusted) * 1000
        audio_espace_temp = AudioSegment.silent(duration=time_less)
        audio_did_ajusted += audio_espace_temp
        # audio_espace_temp += audio_did_ajusted
        audio_espace_temp.export(file_path_to_ajust, format="wav")

def ajust_time_segments (original_audio, output_audio):
    original_audio = AudioSegment.from_file(original_audio)
    duration_original_audio = len(original_audio) / 1000
    out_audio = AudioSegment.from_file(output_audio)
    duration_output_audio = len(out_audio) / 1000
    speed_factor = calculate_speed_factory(
        duration_output_audio, 
        duration_original_audio
        )
    print("speed_factor ======>>>>>>", speed_factor)
    temp_output_path = "result/temp/new_output.wav"
    os.system(f'ffmpeg -i {output_audio} -filter:a "atempo={speed_factor}" {temp_output_path}')
    os.remove(output_audio)
    os.rename(temp_output_path, output_audio)
    
def extract_audio_from_video(video_path, output_relative_path, name_wav):
    if not os.path.exists(output_relative_path):
        os.mkdir(output_relative_path)
    os.system(f"ffmpeg -i {video_path} -q:a 0 -map a {os.path.join(output_relative_path, name_wav)}")
    return os.path.join(output_relative_path, name_wav)
