import whisper
import sys
import json
import torch
from utils.utils_loger import log_error

# Models avaliable
MODEL_TYPES = {
    "tiny": "tiny",
    "base": "base",
    "small": "small",
    "medium": "medium",
    "large": "large"
}

model_type = MODEL_TYPES["large"]
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model(model_type, device=device)
print("==*==*load_model Transcript ==*==*")

def load_and_transcribe(input_audio, source_lang):
    try:
        task = get_task(source_lang)
        
        result = model.transcribe(
            audio=input_audio, 
            language=source_lang, 
            task=task,
            condition_on_previous_text=True,
            fp16=torch.cuda.is_available(),  # Activate fp16 just if GPU be avaliable        
            no_speech_threshold=0.6,
            compression_ratio_threshold=2.4,
            logprob_threshold=-1.0,
            temperature=0.1,
            beam_size=5,
            best_of=3,
            verbose=True
        )

        return result

    except Exception as e:
        log_error(f"An error occurred during transcription: {e}")
        return None

def get_task(source_lang):
    # "translate" or "transcribe"
    if source_lang == "en":
        return "transcribe"
    return "translate"

def validate_input(args):
    if len(args) != 4:
        log_error("Use: transcript.py <input_audio> <source_lang> <file_transcript_name>")
        return sys.exit(1)

def write_transcript_in_file(transcribed_content, file_name):
    if transcribed_content is not None:
        with open(file_name, 'w') as json_file:
            json.dump(transcribed_content, json_file, indent=4)
    else:
        log_error("Transcript fail. Output file did not created.")

def build_trancript(input_audio, source_lang, file_transcript_name):
    if input_audio == None:
        sys.exit(1)
        return
    if source_lang == None:
        sys.exit(1)
        return
    if file_transcript_name == None:
        sys.exit(1)
        return

    transcribed_content = load_and_transcribe(input_audio, source_lang)
    write_transcript_in_file(transcribed_content, file_transcript_name) 

def main():
    validate_input(sys.argv)

    input_audio = sys.argv[1]
    source_lang = sys.argv[2]
    file_transcript_name = sys.argv[3]

    transcribed_content = load_and_transcribe(input_audio, source_lang)
    write_transcript_in_file(transcribed_content, file_transcript_name)
    

if __name__ == "__main__":
    main()
