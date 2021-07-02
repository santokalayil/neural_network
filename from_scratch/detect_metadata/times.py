# import platform  # to detect the operating system
import os
import time


def get_last_modified_time(path_to_file):
    return os.path.getmtime(path_to_file)  # time.ctime(os.path.getmtime(path_to_file))


def get_created_time(path_to_file):
    return os.path.getctime(path_to_file)  # time.ctime(os.path.getctime(path_to_file))
