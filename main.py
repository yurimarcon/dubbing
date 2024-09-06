from config import ORIGINAL_AUDIO, PATH_RELATIVE
from utils_audio import extract_audio_from_video, detect_silences
from splitter_audio import cut_video_at_silence
import sys

def main():
    VIDEO_PATH = sys.argv[1]

    extract_audio_from_video(VIDEO_PATH, ORIGINAL_AUDIO)

    silence_intervals = detect_silences(ORIGINAL_AUDIO)

    cut_video_at_silence(ORIGINAL_AUDIO, silence_intervals, PATH_RELATIVE)

if __name__ == "__main__":
    main()