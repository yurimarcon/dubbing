from googletrans import Translator
from utils.utils_loger import log_error

translator = Translator()

def translate_text (text, source_lang, dest_language):

    src_lang = "en" if source_lang == dest_language else source_lang
    try:
        translated = translator.translate(
            text=text, 
            src=src_lang,
            dest=dest_language
            )
        return translated.text.replace(".", "")
    except Exception as e:
        log_error(f"Google can't translate: '{text}'. Error: {e}")
        return text
