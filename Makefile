run:
	python ./src/main.py
	make clear
merge_video:
	./script/merge_video.sh
clear:
	rm ./m3u8/*;
	rm -rf ./ts/*;
	rm ./video_list/*;
generate:
	mkdir inputa m3u8 output ts url video_list