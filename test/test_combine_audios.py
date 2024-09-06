import unittest
from pydub import AudioSegment
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_voice_generator import combine_audios_and_silences
import json

inputTranscriptText = "data_tests/transcript.json"
inputAudioTest = "data_tests/segment_0.wav"

class TestCombineAudios(unittest.TestCase):

    """
    Audio_durations:
        2454
        3243
        3659
        2273
    """

    def test_start_with_silence_end_finish_with_audio(self):
        """
        Silence_durations:
            1333
            889
            1777
            777
        """
        silences_ranges = [[0.0, 1.333],[4.222, 5.111],[7.222, 8.999], [9.222, 9.999]]
        original_audio = AudioSegment.silent(duration=16405) # Somatory times of silences and audios
        original_audio_path = "data_tests/test_combine_audio/audio.wav"
        original_audio.export(original_audio_path)

        combined_audio = combine_audios_and_silences(
            original_audio_path, 
            f"data_tests/test_combine_audio/4-audios/segment_",
            silences_ranges,
            f"data_tests/test_combine_audio/output.wav"
            )

        combined_audio_duration = len(combined_audio)
        original_audio_duration = len(original_audio)
        self.assertEqual(combined_audio_duration, original_audio_duration)

    def test_start_with_audio_end_finish_with_audio(self):
        """
        Silence_durations:
            889
            1777
            777
        """
        silences_ranges = [[4.222, 5.111],[7.222, 8.999], [9.222, 9.999]]
        original_audio = AudioSegment.silent(duration=15072) # Somatory times of silences and audios
        original_audio_path = "data_tests/test_combine_audio/audio.wav"
        original_audio.export(original_audio_path)

        combined_audio = combine_audios_and_silences(
            original_audio_path, 
            f"data_tests/test_combine_audio/4-audios/segment_",
            silences_ranges,
            f"data_tests/test_combine_audio/output.wav"
            )

        combined_audio_duration = len(combined_audio)
        original_audio_duration = len(original_audio)
        self.assertEqual(combined_audio_duration, original_audio_duration)
    
    def test_start_with_silence_end_finish_with_silence(self):
        """
        Silence_durations:
            1333
            889
            1777
            777
        """
        silences_ranges = [[0.0, 1.333],[4.222, 5.111],[7.222, 8.999],[9.222, 9.999]]
        original_audio = AudioSegment.silent(duration=14132) # Somatory times of silences and audios
        original_audio_path = "data_tests/test_combine_audio/audio.wav"
        original_audio.export(original_audio_path)

        combined_audio = combine_audios_and_silences(
            original_audio_path, 
            f"data_tests/test_combine_audio/3-audios/segment_",
            silences_ranges,
            f"data_tests/test_combine_audio/output.wav"
            )

        combined_audio_duration = len(combined_audio)
        original_audio_duration = len(original_audio)
        self.assertEqual(combined_audio_duration, original_audio_duration)

    def test_start_with_audio_end_finish_with_silence(self):
        """
        Silence_durations:
            333
            889
            1777
            777
        """
        silences_ranges = [[2.000, 2.333],[4.222, 5.111],[7.222, 8.999], [9.222, 9.999]]
        original_audio = AudioSegment.silent(duration=15405) # Somatory times of silences and audios
        original_audio_path = "data_tests/test_combine_audio/audio.wav"
        original_audio.export(original_audio_path)

        combined_audio = combine_audios_and_silences(
            original_audio_path, 
            f"data_tests/test_combine_audio/4-audios/segment_",
            silences_ranges,
            f"data_tests/test_combine_audio/output.wav"
            )

        combined_audio_duration = len(combined_audio)
        original_audio_duration = len(original_audio)
        self.assertEqual(combined_audio_duration, original_audio_duration)

if __name__ == '__main__':
    unittest.main()