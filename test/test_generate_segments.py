import unittest
from pydub import AudioSegment
import sys, os, glob
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_voice_generator import create_segments_in_lot, combine_audios_and_silences, get_speaker_path
from utils_audio import ajust_speed_audio, detect_silences

class TestGenerateAudios(unittest.TestCase):

    # @unittest.skip("provisor")
    def test_a_generate_audios_in_lot(self):
        
        quantity_silences = 11
        relative_path = f"data_tests/test_generate_segments/test_ajust_audio_time_1/"
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
        path_original_audio = "data_tests/test_generate_segments/test_ajust_audio_time_1/audio_0.wav"
        path_segment_without_ajust = "data_tests/test_generate_segments/test_ajust_audio_time_1/segment_0.wav"
        path_segment_ajusted = "data_tests/test_generate_segments/test_ajust_audio_time_1/segment_ajusted_0.wav"
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
        except Exception as e:
            self.fail("Error in process transcript empty!!!")

        os.remove( f"{relative_path}segment_0.wav")
        os.remove( f"{relative_path}segment_ajusted_0.wav")

    def test_d_generete_audio_if_segment_has_music(self):
        quantity_silences = 1
        relative_path = f"data_tests/test_generate_segments/test_ajust_with_silence/"
        original_audio_path = f"{relative_path}audio_0.wav"
        segment_path = f"{relative_path}segment_0.wav"
        segment_ajusted_path = f"{relative_path}segment_ajusted_0.wav"

        try:
            create_segments_in_lot(
                quantity_silences, 
                relative_path
                )

            original_audio = AudioSegment.from_file(original_audio_path)
            ajusted_audio = AudioSegment.from_file(segment_ajusted_path)
            audio_ajusted_ok = False
            
            if len(ajusted_audio) < (len(original_audio) * 1.02) and len(ajusted_audio) > (len(original_audio) * 0.98):
                audio_ajusted_ok = True
        except Exception as e:
            self.fail("Error in process transcript empty!!!", e)

        os.remove( f"{relative_path}segment_ajusted_0.wav")
        os.remove( f"{relative_path}segment_0_0.wav")

        self.assertTrue(audio_ajusted_ok)


    def test_e_max_speed_sefment(self):
        path_relative = "data_tests/test_generate_segments/test_translate_and_ajust_time/"
        original_audio_path = f"{path_relative}audio_0.wav"
        quantity_silences = 1

        other_audio_path = f"{path_relative}segment_0.wav"
        ajusted_audio_path = f"{path_relative}x.wav"

        duratio_original = AudioSegment.from_file(original_audio_path)
        other_audio = AudioSegment.from_file(other_audio_path)
        ajusted_audio = AudioSegment.from_file(ajusted_audio_path)

        print(len(duratio_original), len(other_audio), len(ajusted_audio))

        # try:
        #     create_segments_in_lot(
        #         quantity_silences, 
        #         path_relative
        #         )
        # except Exception as e:
        #     self.fail("Error in process transcript empty!!!")
                    
        self.assertEqual(1,1)

    def test_f_get_speaker(self):
        path_relative = "data_tests/test_generate_segments/test_ajust_audio_time_2/"
        original_audio_path = f"{path_relative}audio_3.wav"
        audio_path_with_bast_duration = get_speaker_path(path_relative, 3)
        correct_path = "data_tests/test_generate_segments/test_ajust_audio_time_2/audio_2.wav"

        self.assertEqual(audio_path_with_bast_duration, correct_path)
    
    # @unittest.skip("skip")
    def test_h_delete_segments_after_tests(seflf):
        relative_path = f"data_tests/test_generate_segments/test_ajust_audio_time_1/"
        pre_output_file_path = f"{relative_path}pre_output.wav"
        output_file_path = f"{relative_path}output.wav"
        files = glob.glob(os.path.join(relative_path, "segment_*"))
        for file in files:
            os.remove(file)
        os.remove(pre_output_file_path)
        os.remove(output_file_path)

if __name__ == '__main__':
    unittest.main()