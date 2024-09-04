from googletrans import Translator

translator = Translator()

def translate_text (text, source_lang, dest_language):
    translated = translator.translate(
        text=text, 
        src=source_lang,
        dest=dest_language
        )
        
    return translated.text.replace(".", "")
