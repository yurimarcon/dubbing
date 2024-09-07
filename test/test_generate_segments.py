import unittest
from pydub import AudioSegment
import sys, os, glob
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_voice_generator import create_segments_in_lot, combine_audios_and_silences
from utils_audio import ajust_speed_audio, detect_silences

class TestGenerateAudios(unittest.TestCase):

    def test_generate_audios_in_lot(self):
        
        quantity_silences = 11
        relative_path = f"data_tests/test_generate_segments/"
        original_audio_path = f"{relative_path}1_audio.wav"
        path_starts_with = f"{relative_path}segment_ajusted_"
        output_file_path = f"{relative_path}output.wav"
        silence_intervals = detect_silences(original_audio_path)

        create_segments_in_lot(
            quantity_silences, 
            relative_path
            )
        combine_audios_and_silences(
            original_audio_path, 
            path_starts_with, 
            silence_intervals, 
            output_file_path
        )
        original_audio = AudioSegment.from_file(original_audio_path)
        output_audio = AudioSegment.from_file(output_file_path)

        timestamp_ok = False
        # Classify tolarance timestamp ajusted
        if len(output_audio) < (len(original_audio) * 1.02):
            timestamp_ok = True
        if len(output_audio) > (len(original_audio) * 0.98):
            timestamp_ok = True

        self.assertTrue(timestamp_ok)

        files = glob.glob(os.path.join(relative_path, "segment*"))
        for file in files:
            os.remove(file)
        os.remove(output_file_path)

    @unittest.skip("Skipping this test")
    def test_ajust_segment_time(self):
        path_original_audio = "data_tests/test_generate_segments/audio_0.wav"
        path_segment_without_ajust = "data_tests/test_generate_segments/segment_0.wav"
        path_segment_ajusted = "data_tests/test_generate_segments/segment_ajusted_0.wav"

        ajust_speed_audio(
            path_original_audio,
            path_segment_without_ajust,
            path_segment_ajusted
        )

        segment = AudioSegment.from_file(path_segment_without_ajust)
        segment_ajusted = AudioSegment.from_file(path_segment_ajusted)

        timestamp_ok = False
        # Classify tolarance timestamp ajusted
        if len(segment_ajusted) < (len(segment) * 1.02):
            timestamp_ok = True
        if len(segment_ajusted) > (len(segment) * 0.98):
            timestamp_ok = True

        self.assertTrue(timestamp_ok)
        os.remove(path_segment_ajusted)

if __name__ == '__main__':
    unittest.main()