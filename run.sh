#!/bin/bash

# Configuration
SOURCE_LANGUAGE="en"
DEST_LANGUAGE="pt"
EXIT_DIR="result/"
TEMP_DIR="temp/"
PATH_INPUT_VIDEO="$1"  # The video must be .mp4
AUDIO_NAME="${TEMP_DIR}audio.wav"
TRANSCRIPT_NAME="${TEMP_DIR}transcript.json"
AUDIO_TRANSLATED_NAME="${TEMP_DIR}output.wav"
VIDEO_RESULT="result.mp4"
PATH_TRANSCRIPT_TEXT="${EXIT_DIR}${TRANSCRIPT_NAME}"
PATH_ORIGINAL_AUDIO="${EXIT_DIR}${AUDIO_NAME}"
PATH_AUDIO_TRANSLATED="${EXIT_DIR}${AUDIO_TRANSLATED_NAME}"
PATH_VIDEO_RESULT="${EXIT_DIR}${VIDEO_RESULT}"
PATH_VIDEO_RESULT_WITHOUT_LIPSINC="${EXIT_DIR}result_without_lipsinc.mp4"

# Define colors
BLUE='\033[34m'
RED='\033[31m'
NC='\033[0m'  # No Color

# Determine the task based on the source language
TASK="transcribe"
if [ "$SOURCE_LANGUAGE" != "en" ]; then
    TASK="translate"
fi

# Define the video creation option
WITH_LIPSINC=2  # 1 for lipsync, 2 for no lipsync, 0 for no video

# Validate user input
function validate_input() {
    if [ -z "$1" ]; then
        echo -e "${RED}You need to pass the .mp4 input file.${NC}"
        exit 1
    fi
}

# Check if the file exists
function validate_input_file_exist() {
    if [ ! -f "$1" ]; then
        echo -e "${RED}The target file does not exist: [ $1 ]${NC}"
        exit 1
    fi
}

# Check if the last command was successful
function validate_error_in_last_command() {
    if [ $? -ne 0 ]; then
        echo -e "${RED}Error in the last command.${NC}"
        exit 1
    fi
}

# Extract audio from the video
function get_audio_from_video() {
    echo -e "${BLUE}Extracting audio from video...${NC}"
    ffmpeg -i "$PATH_INPUT_VIDEO" -ab 160k -ac 2 -ar 44100 -vn "$PATH_ORIGINAL_AUDIO"
    validate_error_in_last_command
}

# Transcribe or translate the audio
function translate_or_transcript() {
    echo -e "${BLUE}${TASK} the audio...${NC}"
    python translate_transcript.py \
        "$PATH_ORIGINAL_AUDIO" \
        "$TASK" \
        "$PATH_TRANSCRIPT_TEXT" \
        "$SOURCE_LANGUAGE" \
        "$DEST_LANGUAGE"
    validate_error_in_last_command
}

# Generate voice from the transcript
function generate_voice_by_transcript() {
    echo -e "${BLUE}Generating voice...${NC}"
    python voice_generator.py \
        "$PATH_ORIGINAL_AUDIO" \
        "$PATH_TRANSCRIPT_TEXT" \
        "$PATH_AUDIO_TRANSLATED" \
        "$SOURCE_LANGUAGE" \
        "$DEST_LANGUAGE"
    validate_error_in_last_command
}

# Create a new video with lipsync
function create_new_video_with_lipsync() {
    echo -e "${RED}Feature in development${NC}"
    exit 
    echo -e "${BLUE}Creating video with lipsync...${NC}"
    cd Wav2Lip || exit
    python3 inference.py \
        --checkpoint_path checkpoints/wav2lip_gan.pth \
        --face "../$PATH_INPUT_VIDEO" \
        --audio "../$PATH_AUDIO_TRANSLATED" \
        --outfile "../$PATH_VIDEO_RESULT" \
        --resize_factor 2
    cd .. || exit
}

# Create a new video without lipsync
function create_new_video_without_lipsync() {
    echo -e "${BLUE}Creating video without lipsync...${NC}"
    ffmpeg -i "$PATH_INPUT_VIDEO" \
        -i "$PATH_AUDIO_TRANSLATED" \
        -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
        -shortest "$PATH_VIDEO_RESULT_WITHOUT_LIPSINC"
}

# Remove temporary files after the process
function delete_files_after_process() {
    rm "$PATH_TRANSCRIPT_TEXT"
}

# Start the process
validate_input "$1"
validate_input_file_exist "$1"

echo -e "${BLUE}Starting the process...${NC}"
get_audio_from_video
translate_or_transcript
generate_voice_by_transcript

case $WITH_LIPSINC in
    1) create_new_video_with_lipsync ;;
    2) create_new_video_without_lipsync ;;
    *) echo -e "${BLUE}Video not created.${NC}"
esac

# delete_files_after_process
echo -e "${BLUE}Process completed!!!${NC}"
