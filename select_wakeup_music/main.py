import os
from glob import glob
import random
import shutil

TAG = "WakeUpMusicSelecter"
SRC_LIB_DIR = "D:\\ide\\Music\\"
DST_DIR = "C:\\Users\\ide\\works\\python_sample\\select_wakeup_music\\"
DST_NAME = "alerm"

dir_list = os.listdir(SRC_LIB_DIR)
music_files = []
for dir in dir_list:
    files_in_dir = glob(SRC_LIB_DIR + dir + "\\*.mp3")
    music_files.extend(files_in_dir)
    #files_in_dir = glob(SRC_LIB_DIR + dir + "\\*.flac")
    #music_files.extend(files_in_dir)
num_music = len(music_files)
print("{}: found {} music.".format(TAG, num_music))

src_id = random.randint(0, num_music - 1)
src_file = music_files[src_id]
print("{}: selected: {}".format(TAG, src_file))

src_root, src_ext = os.path.splitext(src_file)
dst_file = DST_DIR + DST_NAME + src_ext
shutil.copyfile(src_file, dst_file)
print("{}: copied to: {}".format(TAG, dst_file))
