import os

# Paths and filenames
VOICE_MODEL = "model_voice/model.wav"
SOURCE_FOLDER = "result/"
TEMP_FOLDER = "temp/"
PATH_RELATIVE = os.path.join(SOURCE_FOLDER, TEMP_FOLDER)
FILE_NAME_SEGMENT = "segment_"
FILE_NAME_ADJUSTED_TEMP = "segment_ajust_temp_"
FILE_NAME_ADJUSTED = "segment_ajusted_"
SILENCE_NAME="silence_"
SPLITED_INITIAL_AUDIO_NAME="audio_"
ORIGINAL_AUDIO_NAME = "1_audio.wav"
ORIGINAL_AUDIO = os.path.join(PATH_RELATIVE, "1_audio.wav")
OUTPUT_AUDIO = os.path.join(PATH_RELATIVE, "output.wav")