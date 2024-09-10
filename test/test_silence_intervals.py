import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_audio import detect_silences

class TestSilenceIntervals(unittest.TestCase):

    def test_split_audio_one_silence_in_mid(self):

        audio_path = "data_tests/test_spliter_audio/test_possibilities_split/1_audio.wav"
        silence_intervals = detect_silences(audio_path)
        self.assertEqual(len(silence_intervals),24)

    def test_audio_without_silences(self):
        audio_path = "data_tests/test_spliter_audio/test_without_silences/1_audio.wav"
        silence_intervals = detect_silences(audio_path)
        self.assertEqual(len(silence_intervals),0)

if __name__ == '__main__':
    unittest.main()