from googletrans import Translator

translator = Translator()

def translate_text (text, source_lang, dest_language):
    try:
        translated = translator.translate(
            text=text, 
            src=source_lang,
            dest=dest_language
            )
            
        return translated.text.replace(".", "")
    except Exception as e:
        print(f"An error occurred during translating: {e}")
        return " .Google translate can't translate it. "
