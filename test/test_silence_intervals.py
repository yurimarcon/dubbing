import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_audio import detect_silences

class TestSilenceIntervals(unittest.TestCase):

    def test_split_audio_one_silence_in_mid(self):

        audio_path = "data_tests/test_spliter_audio/1_audio.wav"
        silence_intervals = detect_silences(audio_path)
        print(silence_intervals)

        self.assertEqual(len(silence_intervals),13)

if __name__ == '__main__':
    unittest.main()