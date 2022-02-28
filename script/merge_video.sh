#!/bin/zsh
cd ./video_list || exit;
for file in ./*
do
    echo "$file"
    ffmpeg -f concat -safe 0 -i "$file" -c copy ../output/"$file".mp4
done
