import unittest
from pydub import AudioSegment
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_audio import get_speed_factory, ajust_speed_audio, calculate_speed_factory
import json

inputTranscriptText = "data_tests/transcript.json"
inputAudioTest = "data_tests/segment_0.wav"

with open(inputTranscriptText, 'r') as file:    
    result = json.load(file)

segments = result['segments']

class TestAudioUtils(unittest.TestCase):

    # Minor then speed_factory 0.9 make audio verry slow
    def test_get_speed_factory_small(self):
        segments[0]['start'] = 0
        segments[0]['end'] = 3.5
        speed_factor = get_speed_factory(segments[0], inputAudioTest)
        self.assertEqual(speed_factor, 0.9)

    # More then speed_factory 1.3 make audio verry fast
    def test_get_speed_factory_large(self):
        segments[0]['start'] = 0
        segments[0]['end'] = 2.3
        speed_factor = get_speed_factory(segments[0], inputAudioTest)
        self.assertEqual(speed_factor, 1.35)

    # verify if the audio ajusted be between time tolerate
    def test_ajust_audio_time(self):
        original_audio = AudioSegment.silent(duration=10000)
        path_audio_original = "data_tests/test_audio_utils/original_audio.wav"
        original_audio.export(path_audio_original)
        other_audio = AudioSegment.silent(duration=9000)
        path_other_audio = "data_tests/test_audio_utils/other_audio.wav"
        original_audio.export(path_other_audio)

        path_new_audio = "data_tests/test_audio_utils/audio_ajusted_time.wav"

        ajust_speed_audio(path_other_audio, path_audio_original, path_new_audio)
        audio_ajusted = AudioSegment.from_file(path_new_audio)

        timestamp_ok = False
        # Classify tolarance timestamp ajusted
        if len(audio_ajusted) < (len(original_audio) * 1.02):
            timestamp_ok = True
        if len(audio_ajusted) > (len(original_audio) * 0.98):
            timestamp_ok = True

        self.assertTrue(timestamp_ok)
        os.remove(path_new_audio)

    # Calculate speed_factory
    def test_get_speed_factory_small(self):
        speed_factor = calculate_speed_factory(9000, 10000)
        self.assertEqual(speed_factor, 0.9)

if __name__ == '__main__':
    unittest.main()