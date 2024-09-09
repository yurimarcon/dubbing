#!/bin/bash

# ffmpeg -i $1 -ss 00:00:05 -c:v libx264 -c:a aac -strict experimental $2

for i in ./*.mp4
do
    # remove first seconds of video
    new_name=$(echo "$i" | cut -c 1-$((${#i}-5)))
    ffmpeg -i $i -ss 00:00:05 -c:v libx264 -c:a aac -strict experimental "${new_name}1.mp4"
    # mv "${i}" "${new_name}.mp4"
    echo $new_name
done
