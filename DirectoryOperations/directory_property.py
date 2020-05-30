# coding=UTF-8
import os
from os.path import join, getsize

# MinimumSize = 512000
MinimumSize = 4194304
MaximumSize = 5368709120


def filterSubFolders(root, condition):
    folders = []
    for root, dirs, files in os.walk(root):
        if not dirs and eval(condition):
            folders.append(root)
    return folders


def subFolderSize(sub):
    size = 0
    for root, dirs, files in os.walk(sub):
        size += sum([getsize(join(root, name)) for name in files])
    return size


def deleteFiles(dir: str):
    for root, dirs, files in os.walk(dir):
        for file in files:
            # print(file)
            # if file.find(FixedNamePattern) > -1:
            if file.find('.torrent') > -1:
                # print(getFullPath(root, file))
                os.remove(getFullPath(root, file))
        # print(files)


def getFullPath(folder, filename):
    return folder + '\\' + filename


if __name__ == '__main__':
    path = r'E:\迅雷下载'
    deleteFiles(path)
    # path = r'F:\你懂的'
    # print('-------Below folder is less than %d KB-------' % (MinimumSize / 1024))
    # for directory in filterSubFolders(path, 'subFolderSize(root) < MinimumSize'):
    #     print(directory)

    # print('-------Below folder is lager than %d MB-------' % (MaximumSize / 1024 / 1024))
    # for directory in filterSubFolders(path, 'subFolderSize(root) > MaximumSize'):
    #     print(directory)
