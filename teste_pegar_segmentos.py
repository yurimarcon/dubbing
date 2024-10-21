from utils.utils_transcript import load_and_transcribe


input_audio = "result/1_audio.wav"
source_lang = "en"
x = load_and_transcribe(input_audio, source_lang)
print(x)