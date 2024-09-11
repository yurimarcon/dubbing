from googletrans import Translator
from utils_loger import log_error

translator = Translator()

def translate_text (text, source_lang, dest_language):
    try:
        translated = translator.translate(
            text=text_cleaned, 
            src=source_lang,
            dest=dest_language
            )
        return translated.text.replace(".", "")
    except Exception as e:
        log_error(f"Google can't translate: '{text}'. Error: {e}")
        return " .Google translate can't translate it. "
