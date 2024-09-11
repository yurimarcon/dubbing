import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from transcript import build_trancript, get_task

class TestTranslate(unittest.TestCase):

    def test_transcript_calling_file(self):
        path_relative = "data_tests/test_spliter_audio/test_without_silences/"
        original_audio_path = f"{path_relative}1_audio.wav"
        result = os.system(
                f"python ../transcript.py {path_relative}1_audio.wav en {path_relative}transcript_0.json")
        self.assertEqual(result,0)

    def test_transcript_callog_method(self):
        path_relative = "data_tests/test_spliter_audio/test_without_silences/"
        original_audio_path = f"{path_relative}1_audio.wav"
        result =  build_trancript(f"{path_relative}1_audio.wav", "en", f"{path_relative}transcript_0.json")
        self.assertEqual(result, None)

    def test_get_task_transcribe(self):
        source_lang = "en"
        task = get_task(source_lang)
        self.assertEqual(task, "transcribe")
    
    def test_get_task_translate_pt(self):
        source_lang = "pt"
        task = get_task(source_lang)
        self.assertEqual(task, "translate")

    def test_get_task_translate_es(self):
        source_lang = "es"
        task = get_task(source_lang)
        self.assertEqual(task, "translate")

    def test_z_delete_transcript(self):
        path_relative = "data_tests/test_spliter_audio/test_without_silences/"
        os.remove(f"{path_relative}transcript_0.json")

if __name__ == '__main__':
    unittest.main()