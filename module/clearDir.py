# clear "work_dir"
import os, glob


def get_clear_dir():
    dir = '/home/adrian/Pulpit/selenium_olx/work_dir'
    filelist = glob.glob(os.path.join(dir, "*"))
    for files in filelist:
        os.remove(files)


get_clear_dir()
