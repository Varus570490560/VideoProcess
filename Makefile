run:
	python ./src/main.py
merge_video:
	./script/merge_video.sh
clear:
	rm ./input/*;
	rm ./m3u8/*;
	rm ./output/*;
	rm -r ./ts/*;
	rm ./video_list/*;