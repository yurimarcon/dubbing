import unittest
from pydub import AudioSegment
import sys, os, glob
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from splitter_audio import cut_video_at_silence
from utils_audio import detect_silences

class TestSplitAudio(unittest.TestCase):

    def test_split_audio_one_silence_in_mid(self):
        silence_intervals = [[372.065, 373.136]]

        audio_path = "data_tests/test_spliter_audio/test_possibilities_split/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/test_possibilities_split/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)

        self.assertEqual(quantity_parts_videos,2)

    def test_split_audio_when_has_one_audio_in_start(self):
        silence_intervals = [[0.0, 3.136]]

        audio_path = "data_tests/test_spliter_audio/test_possibilities_split/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/test_possibilities_split/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
        self.assertEqual(quantity_parts_videos,1)

    def test_split_audio_when_has_one_silence_in_start_and_one_in_end(self):
        silence_intervals = [[0.0, 10.0],[98.0, 108.0]]

        audio_path = "data_tests/test_spliter_audio/test_possibilities_split/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/test_possibilities_split/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
        self.assertEqual(quantity_parts_videos,1)

    def test_split_audio_when_has_one_silence_in_the_end(self):
        silence_intervals = [[98.0, 108.0]]

        audio_path = "data_tests/test_spliter_audio/test_possibilities_split/1_audio.wav"
        output_folder = "data_tests/test_spliter_audio/test_possibilities_split/"
        quantity_parts_videos = cut_video_at_silence(audio_path, silence_intervals, output_folder)
        self.assertEqual(quantity_parts_videos,1)
    
    def test_spliter_audio_original_1(self):
        path_relative = "data_tests/test_spliter_audio/test_quantity_splited/"
        original_audio_path = f"{path_relative}1_audio.wav"
        original_audio = AudioSegment.from_file(original_audio_path)
        silence_intervals = detect_silences(original_audio_path)

        quantity_sliced_audios = cut_video_at_silence(original_audio_path, silence_intervals, path_relative)

        files_to_remove = glob.glob("data_tests/test_spliter_audio/test_quantity_splited/audio_*")
        for file in files_to_remove:
            print("Removing file: ",file)
            os.remove(file)

        self.assertEqual(quantity_sliced_audios, 8)

    def test_spliter_audio_original2(self):
        path_relative = "data_tests/test_spliter_audio/test_quantity_splited/"
        original_audio_path = f"{path_relative}2_audio.wav"
        silence_intervals = detect_silences(original_audio_path)

        quantity_sliced_audios = cut_video_at_silence(original_audio_path, silence_intervals, path_relative)

        files_to_remove = glob.glob("data_tests/test_spliter_audio/test_quantity_splited/audio_*")
        for file in files_to_remove:
            os.remove(file)

        self.assertEqual(quantity_sliced_audios, 7)

        
    def test_prevent_create_last_audio_chunk_with_zero_seconds(self):
        path_relative = "data_tests/test_segment_zero_audio/test_prevent_last_chunk_zero_seconds/"
        original_audio_path = f"{path_relative}1_audio.wav"
        silence_intervals = detect_silences(original_audio_path)

        quantity_sliced_audios = cut_video_at_silence(original_audio_path, silence_intervals, path_relative)

        original_audio = AudioSegment.from_file(f"{path_relative}audio_6.wav")

        files_to_remove = glob.glob(f"{path_relative}audio_*")
        for file in files_to_remove:
            os.remove(file)

        self.assertGreater(len(original_audio),0)

    def tearDown(self):
        files_to_remove = glob.glob("data_tests/test_spliter_audio/test_possibilities_split/audio_*")

        for file in files_to_remove:
            os.remove(file)

if __name__ == '__main__':
    unittest.main()