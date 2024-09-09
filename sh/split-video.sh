#!/bin/bash

# ORIGIN_PATH="/Users/yurimarcon/Documents/Udemy/Curso_vue/Vídeos/"
# FUTURE_PATH="/Users/yurimarcon/Documents/Udemy/Curso_vue/Vídeos/"
ORIGIN_PATH="result/"
FUTURE_PATH="result/"
INPUT_FILE_NAME="v.mp4"
INPUT_VIDEO="${ORIGIN_PATH}${INPUT_FILE_NAME}"
VIDEO_NUMBER="0"
OUTPUT_VIDEO_PART1="${FUTURE_PATH}${VIDEO_NUMBER}-1.mp4"
OUTPUT_VIDEO_PART2="${FUTURE_PATH}${VIDEO_NUMBER}-2.mp4"
OUTPUT_VIDEO_PART3="${FUTURE_PATH}${VIDEO_NUMBER}-3.mp4"
OUTPUT_VIDEO_PART4="${FUTURE_PATH}${VIDEO_NUMBER}-4.mp4"
# OUTPUT_VIDEO_PART5="${FUTURE_PATH}${VIDEO_NUMBER}-5.mp4"

# ffmpeg -i "$INPUT_VIDEO" -ss 00:00:00 -to 00:04:59 -c copy ${OUTPUT_VIDEO_PART1}
# ffmpeg -i "$INPUT_VIDEO" -ss 00:04:59 -c copy ${OUTPUT_VIDEO_PART2}


ffmpeg -i "$INPUT_VIDEO" -ss 00:00:00 -to 00:00:59 -c copy ${OUTPUT_VIDEO_PART1}
ffmpeg -i "$INPUT_VIDEO" -ss 00:00:59 -to 00:01:58 -c copy ${OUTPUT_VIDEO_PART2}
ffmpeg -i "$INPUT_VIDEO" -ss 00:01:58 -to 00:02:57 -c copy ${OUTPUT_VIDEO_PART3}
# ffmpeg -i "$INPUT_VIDEO" -ss 00:14:56 -to 00:19:55 -c copy ${OUTPUT_VIDEO_PART4}
ffmpeg -i "$INPUT_VIDEO" -ss 00:01:58 -c copy ${OUTPUT_VIDEO_PART4}

## Split and manteining all the frames, do not make firsts seconds black screen
# ffmpeg -i v.mp4 -ss 00:00:59 -to 00:01:58 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -c:a aac t.mp4

# count=5

# while [ $count -le 18 ]
# do
#     INPUT_FILE_NAME=`ls "$ORIGIN_PATH" | head -n 1`

#     ffmpeg -i "${ORIGIN_PATH}${INPUT_FILE_NAME}" -ss 00:00:00 -to 00:04:59 -c copy ${OUTPUT_VIDEO_PART1}
#     ffmpeg -i "${ORIGIN_PATH}${INPUT_FILE_NAME}" -ss 00:04:59 -c copy ${OUTPUT_VIDEO_PART2}

#     cp "${ORIGIN_PATH}${INPUT_FILE_NAME}" "$FUTURE_PATH"
    
#     echo "Contagem: $count"
#     ((count++))
# done
