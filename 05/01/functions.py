import os

def create_dirs():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        os.mkdir(dir_name)

def remove_dirs():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        os.rmdir(dir_name)