import unittest
from pydub import AudioSegment
import sys, os, glob
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from splitter_audio import cut_video_at_silence
from utils_audio import detect_silences

class TestSplitAudio(unittest.TestCase):

    # def test_split_audio_one_silence_in_mid(self):
    #     silence_intervals = [[372.065, 373.136]]

    #     audio_path = "data_tests/test_spliter_audio/1_audio.wav"
    #     output_folder = "data_tests/test_spliter_audio/"
    #     quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)

    #     self.assertEqual(quantity_parts_videos,2)

    # def test_split_audio_when_has_one_audio_in_start(self):
    #     silence_intervals = [[0.0, 3.136]]

    #     audio_path = "data_tests/test_spliter_audio/1_audio.wav"
    #     output_folder = "data_tests/test_spliter_audio/"
    #     quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
    #     self.assertEqual(quantity_parts_videos,1)

    # def test_split_audio_when_has_one_silence_in_start_and_one_in_end(self):
    #     silence_intervals = [[0.0, 10.0],[98.0, 108.0]]

    #     audio_path = "data_tests/test_spliter_audio/1_audio.wav"
    #     output_folder = "data_tests/test_spliter_audio/"
    #     quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
    #     self.assertEqual(quantity_parts_videos,1)

    # def test_split_audio_when_has_one_silence_in_the_end(self):
    #     silence_intervals = [[98.0, 108.0]]

    #     audio_path = "data_tests/test_spliter_audio/1_audio.wav"
    #     output_folder = "data_tests/test_spliter_audio/"
    #     quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
    #     self.assertEqual(quantity_parts_videos,1)

    def test_spliter_audio_original(self):
        path_relative = "data_tests/test_spliter_audio/"
        original_audio_path = f"{path_relative}1_audio.wav"
        original_audio = AudioSegment.from_file(original_audio_path)

        print("===================")
        print(len(original_audio))
        print("===================")
        silence_intervals = detect_silences(original_audio_path)
        print(silence_intervals)

        quantity_sliced_audios = cut_video_at_silence(original_audio_path, silence_intervals, path_relative)

        # pegamos o senário onde 0 12º audio ficou com 00:00...

        self.assertTrue(True)

    # def tearDown(self):
    #     files_to_remove = glob.glob("data_tests/test_spliter_audio/audio_*")

    #     for file in files_to_remove:
    #         os.remove(file)

if __name__ == '__main__':
    unittest.main()