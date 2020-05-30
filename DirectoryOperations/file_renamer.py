# coding=UTF-8
import os
import re

FixedNamePattern = '[阳光电影-www.ygdy8.com]'
AlbumPattern = r'[A-Za-z]{3,}[-_]?\d{3,}[AB]?[_\d]?'
FileExtensionPattern = '\.\w{3,}'


def filterFiles(root, condition):
    files = []
    for root, dirs, files in os.walk(root):
        for file in files:
            if file.find(FixedNamePattern) > -1:
                # print('origin filename is %s' % file)
                filename = file.replace(FixedNamePattern, '')
                os.rename(getFullPath(root, file), getFullPath(root, filename))
        for dir in dirs:
            if dir.find(FixedNamePattern) > -1:
                print('origin folder is %s' % dir)


def renameFiles(root):
    files = []
    for root, dirs, files in os.walk(root):
        for f in files:
            album = getAlbum(f, False)
            if album:
                # print(album['filename'])
                try:
                    os.rename(getFullPath(root, f), getFullPath(
                        root, album['filename']))
                except:
                    print(f)
                    pass
        for d in dirs:
            album = getAlbum(d, True)

            if album:
                try:
                    os.rename(getFullPath(root, d), getFullPath(
                        root, album['filename']))
                except:
                    print(d)
                    pass
                # print(album['filename'])


def getAlbum(name: str, isDirectory: bool):
    albums = re.findall(AlbumPattern, name)
    extension = None
    shouldHasExtension = not isDirectory
    if shouldHasExtension:
        extension = re.findall(FileExtensionPattern, name)

    if albums and len(albums) >= 1:
        filename = albums[-1]
        if shouldHasExtension:
            filename += extension[-1]
        return {
            'filename': filename,
            'shouldHasExtension': shouldHasExtension,
            'extension': extension
        }
    else:
        print('Unable to match: %s' % name)
        return None


def getFullPath(folder, filename):
    return folder + '\\' + filename


if __name__ == '__main__':
    path = r'E:\迅雷下载'
    renameFiles(path)
