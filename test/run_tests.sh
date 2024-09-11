#!/bin/bash

time python -m unittest \
    test_translate_utils.py \
    test_text_utils.py \
    test_audio_utils.py \
    test_combine_audios.py \
    test_generate_segments.py \
    test_spliter_audio.py \
    test_silence_intervals.py \
    test_transcript.py