# coding=UTF-8
import os
from os.path import join, getsize

# MinimumSize = 512000
MinimumSize = 4096000
MaximumSize = 5368709120


def filterSubFolders(root, condition):
    empties = []
    for root, dirs, files in os.walk(root):
        if not dirs and eval(condition):
            empties.append(root)
    return empties


def subFolderSize(sub):
    size = 0
    for root, dirs, files in os.walk(sub):
        size += sum([getsize(join(root, name)) for name in files])
    return size


if __name__ == '__main__':
    path = r'D:\迅雷下载'
    # for directory in filterSubFolders(path, 'subFolderSize(root) < MinimumSize'):
    #     print(directory)
    for directory in filterSubFolders(path, 'subFolderSize(root) > MaximumSize'):
        print(directory)
