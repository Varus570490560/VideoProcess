import os

import analysis_master_m3u8
import config_parse
if __name__ == '__main__':
    analysis_master_m3u8.analysis_master()
    analysis_master_m3u8.analysis_m3u8()
    analysis_master_m3u8.generate_video_list()
    os.system(config_parse.get_path()+'/VideoProcess/script/merge_video.sh')


