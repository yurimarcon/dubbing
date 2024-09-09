import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestTranslate(Test.case):
    path_relative = "data_tests/test_spliter_audio/"
    original_audio_path = f"{path_relative}1_audio.wav"
    quantity_sliced_audios = 12

    for idx in range(quantity_sliced_audios):
        os.system(
                f"python transcript.py {path_relative}audio_{idx}.wav translate {path_relative}transcript_{idx}.json en pt")

    pass

if __name__ == '__main__':
    unittest.main()