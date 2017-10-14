# -*- coding=UTF-8-*-

# 中文
import os

print os.name

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# print os.uname()
# 解析Path
# print os.getenv('PATH')

# d = os.environ
# print type(d)

# print os.getcwd()

# print os.path.join("C:\\", "IDE")
#
# fromFolder = os.path.join("C:\\", "IDE")
# fromName = os.path.join(fromFolder, "test.txt")
#
# toName = os.path.join(fromFolder, "test.py")
# print fromName
# os.rename(fromName, toName)

#
# fromFolder = os.path.join("C:\\", "IDE")
# toFolder = os.path.abspath('.')
# distFileName = os.path.join(os.getcwd(), 'test.py')
# shutil.copyfile(toName, distFileName)

# os.remove('test.py')
print  os.listdir('.')

print [x for x in os.listdir('.') if os.path.isdir(x)]

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

# 练习：编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
# TODO
# $ python search.py test
# unit_test.log
# py/test.py
# py/test_os.py
# my/logs/unit-test-result.txt
