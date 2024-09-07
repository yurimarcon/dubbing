import whisper
import sys
import json
import torch

# Models avaliable
MODEL_TYPES = {
    "tiny": "tiny",
    "base": "base",
    "small": "small",
    "medium": "medium",
    "large": "large"
}

def load_and_transcribe(input_audio, source_lang, task):
    try:
        model_type = MODEL_TYPES["medium"]
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = whisper.load_model(model_type, device=device)
        
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
        print(f"An error occurred during transcription: {e}")
        return None

def main():
    if len(sys.argv) != 6:
        print("Use: transcript.py <input_audio> <task> <file_transcript_name> <source_lang> <dest_language>")
        sys.exit(1)

    input_audio = sys.argv[1]
    task = sys.argv[2] if sys.argv[2] else "translate"  # "translate" ou "transcribe"
    file_transcript_name = sys.argv[3]
    source_lang = sys.argv[4]
    dest_language = sys.argv[5]

    transcribed_content = load_and_transcribe(input_audio, source_lang, task)

    if transcribed_content is not None:
        with open(file_transcript_name, 'w') as json_file:
            json.dump(transcribed_content, json_file, indent=4)
    else:
        print("Transcript fail. Output file did not created.")

if __name__ == "__main__":
    main()
