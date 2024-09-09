#!/bin/bash

RELATIVE_PATH="/Users/yurimarcon/Documents/Udemy/Curso_vue/Vídeos/En-Sessao-3/"
VIDEO_NUMBER="18"
RESULT_FILE_NAME="${VIDEO_NUMBER}-Resposivity.mp4"
QUANTITY_VIDEOS=4

function concat_video (){
    ffmpeg \
        -i "$1" \
        -i "$2" \
        -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[outv][outa]" \
        -map "[outv]" \
        -map "[outa]" "$3"
}

count=1
loops=$(($QUANTITY_VIDEOS-1))

while [ $count -le $loops ] 
do
    echo "===================="
    if [ $count -eq 1 ] && [ $count -eq $loops ]; then
        next_number=$(($count+1))
        atual_video1="$RELATIVE_PATH""${VIDEO_NUMBER}-${count}-cap.mp4"
        atual_video2="$RELATIVE_PATH""${VIDEO_NUMBER}-${next_number}-cap.mp4"
        output_video="${RELATIVE_PATH}${RESULT_FILE_NAME}"
    elif [ $count -eq 1 ]; then
        next_number=$(($count+1))
        atual_video1="$RELATIVE_PATH""${VIDEO_NUMBER}-${count}-cap.mp4"
        atual_video2="$RELATIVE_PATH""${VIDEO_NUMBER}-${next_number}-cap.mp4"
        output_video="$RELATIVE_PATH""${VIDEO_NUMBER}-temp${count}.mp4"
    elif [ $count -le $(($loops-1)) ]; then
        previous_number=$(($count-1))
        next_number=$(($count+1))
        atual_video1="${RELATIVE_PATH}${VIDEO_NUMBER}-temp${previous_number}.mp4"
        atual_video2="${RELATIVE_PATH}${VIDEO_NUMBER}-${next_number}-cap.mp4"
        output_video="$RELATIVE_PATH""${VIDEO_NUMBER}-temp${count}.mp4"
    else
        previous_number=$(($count-1))
        next_number=$(($count+1))
        atual_video1="${RELATIVE_PATH}${VIDEO_NUMBER}-temp${previous_number}.mp4"
        atual_video2="${RELATIVE_PATH}${VIDEO_NUMBER}-${next_number}-cap.mp4"
        output_video="${RELATIVE_PATH}${RESULT_FILE_NAME}"
    fi
    echo $atual_video1 $atual_video2 $output_video
    concat_video $atual_video1 $atual_video2 $output_video
    ((count++))
    echo "===================="
done 
