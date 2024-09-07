import unittest
import sys, os, glob
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from splitter_audio import cut_video_at_silence

class TestSplitAudio(unittest.TestCase):

    def test_split_audio_one_silence_in_mid(self):
        silence_intervals = [[372.065, 373.136]]

        audio_path = "data_tests/test_spliter_audio/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)

        self.assertEqual(quantity_parts_videos,2)

    def test_split_audio_when_has_one_audio_in_start(self):
        silence_intervals = [[0.0, 3.136]]

        audio_path = "data_tests/test_spliter_audio/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
        self.assertEqual(quantity_parts_videos,1)

    def test_split_audio_when_has_one_silence_in_start_and_one_in_end(self):
        silence_intervals = [[0.0, 10.0],[854.0, 864.0]]

        audio_path = "data_tests/test_spliter_audio/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
        self.assertEqual(quantity_parts_videos,1)

    def test_split_audio_when_has_one_silence_in_the_end(self):
        silence_intervals = [[854.0, 864.0]]

        audio_path = "data_tests/test_spliter_audio/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
        self.assertEqual(quantity_parts_videos,1)

    def tearDown(self):
        files_to_remove = [
            "data_tests/test_spliter_audio/audio_0.wav",
            "data_tests/test_spliter_audio/audio_1.wav"
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                try:
                    os.remove(file)
                    print(f"{file} removido com sucesso.")
                except Exception as e:
                    print(f"Erro ao tentar remover {file}: {e}")

if __name__ == '__main__':
    unittest.main()