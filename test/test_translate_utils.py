import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_translate import translate_text

class TestTranslateUtils(unittest.TestCase):

    def test_translate_english_to_espanish (self):
        text = "Hello World!!!"
        text_translated = translate_text(text, "en", "es")
        self.assertEqual(text_translated, "¡¡¡Hola Mundo!!!")

    def test_translate_english_to_portuguese (self):
        text = "Hello World!!!"
        text_translated = translate_text(text, "en", "pt")
        self.assertEqual(text_translated, "Olá mundo !!!")
    
    def test_translate_english_to_portuguese (self):
        text = "Great..."
        text_translated = translate_text(text, "en", "pt")
        print(text_translated)
        self.assertEqual(text_translated, "Ótimo")

if __name__ == '__main__':
    unittest.main()