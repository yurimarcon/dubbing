from config import ORIGINAL_AUDIO, PATH_RELATIVE
from utils_audio import extract_audio_from_video, detect_silences
from utils_voice_generator import generate_audio_by_text
from splitter_audio import cut_video_at_silence
import sys
import os
import json

def main():
    VIDEO_PATH = sys.argv[1]

    # extract_audio_from_video(VIDEO_PATH, ORIGINAL_AUDIO)

    silence_intervals = detect_silences(ORIGINAL_AUDIO)

    quantity_sliced_audios = cut_video_at_silence(ORIGINAL_AUDIO, silence_intervals, PATH_RELATIVE)
    print("quantity_sliced_audios ", quantity_sliced_audios)

    for idx in range(quantity_sliced_audios):
        os.system(
            f"python transcript.py {PATH_RELATIVE}audio_{idx}.wav translate {PATH_RELATIVE}transcript_{idx}.json pt en")

    for idx in range(quantity_sliced_audios):
        with open(f"{PATH_RELATIVE}transcript_{idx}.json", 'r') as file:    
            text = json.load(file)['text']
        
        generate_audio_by_text(
            text, 
            f"{PATH_RELATIVE}audio_{idx}.wav", 
            f"{PATH_RELATIVE}segment_{idx}", 
            "pt", 
            "en"
            )

if __name__ == "__main__":
    main()