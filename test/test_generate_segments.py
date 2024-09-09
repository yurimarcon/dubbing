import unittest
from pydub import AudioSegment
import sys, os, glob
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_voice_generator import create_segments_in_lot, combine_audios_and_silences
from utils_audio import ajust_speed_audio, detect_silences

class TestGenerateAudios(unittest.TestCase):

    # @unittest.skip("provisor")
    def test_a_generate_audios_in_lot(self):
        
        quantity_silences = 11
        relative_path = f"data_tests/test_generate_segments/"
        original_audio_path = f"{relative_path}1_audio.wav"
        path_starts_with = f"{relative_path}segment_ajusted_"
        pre_output_file_path = f"{relative_path}pre_output.wav"
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
            pre_output_file_path
        )
        speed_factory = ajust_speed_audio(
            pre_output_file_path,
            original_audio_path,
            output_file_path
        )
        original_audio = AudioSegment.from_file(original_audio_path)
        output_audio = AudioSegment.from_file(output_file_path)
        original_duration = len(original_audio)
        output_duration = len(output_audio)
        max_tolerance = original_duration * 1.02
        min_tolerance = original_duration * 0.98

        timestamp_ok = False
        # Classify tolarance timestamp ajusted
        if speed_factory == 1.3 or speed_factory == 0.9:
            timestamp_ok = True
        elif output_duration < max_tolerance and output_duration > min_tolerance:
            timestamp_ok = True
        else:
            print("Test do not pass becouse time without tolerance: ", output_duration)
            print("Expeted time less then: ", max_tolerance)
            print("Expeted time more then: ", min_tolerance)

        self.assertTrue(timestamp_ok)

    # @unittest.skip("provisor")
    def test_b_ajust_segment_time(self):
        path_original_audio = "data_tests/test_generate_segments/audio_0.wav"
        path_segment_without_ajust = "data_tests/test_generate_segments/segment_0.wav"
        path_segment_ajusted = "data_tests/test_generate_segments/segment_ajusted_0.wav"
        os.remove(path_segment_ajusted)
        
        speed_factory = ajust_speed_audio(
            path_segment_without_ajust,
            path_original_audio,
            path_segment_ajusted
        )

        original_audio = AudioSegment.from_file(path_original_audio)
        segment_ajusted = AudioSegment.from_file(path_segment_ajusted)
        original_duration = len(original_audio)
        segment_ajusted_duration = len(segment_ajusted)
        max_tolerance = original_duration * 1.02
        min_tolerance = original_duration * 0.98

        timestamp_ok = False
        # Classify tolarance timestamp ajusted
        if speed_factory == 1.3 or speed_factory == 0.9:
            timestamp_ok = True
        elif segment_ajusted_duration < max_tolerance and segment_ajusted_duration > min_tolerance:
            timestamp_ok = True
        else:
            print("Test do not pass becouse time without tolerance: ", segment_ajusted_duration)
            print("Expeted time less then: ", max_tolerance)
            print("Expeted time more then: ", min_tolerance)

        self.assertTrue(timestamp_ok)

    def test_c_empty_transcription(self):
        quantity_silences = 1
        relative_path = f"data_tests/test_segment_zero_audio/"

        try:
            create_segments_in_lot(
                quantity_silences, 
                relative_path
                )
        except e:
            self.fail("Error in process transcript empty!!!")

        os.remove( f"{relative_path}segment_0.wav")
        os.remove( f"{relative_path}segment_ajusted_0.wav")
    
    # @unittest.skip("skip")
    def test_d_delete_segments_after_tests(seflf):
        relative_path = f"data_tests/test_generate_segments/"
        pre_output_file_path = f"{relative_path}pre_output.wav"
        output_file_path = f"{relative_path}output.wav"
        files = glob.glob(os.path.join(relative_path, "segment_*"))
        for file in files:
            os.remove(file)
        os.remove(pre_output_file_path)
        os.remove(output_file_path)

if __name__ == '__main__':
    unittest.main()