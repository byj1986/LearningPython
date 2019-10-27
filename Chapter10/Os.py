import os
import pprint
import webbrowser

pprint.pprint(os.environ)

print('folder path separator', os.sep)
print('path separator', os.pathsep)
print('line separator', os.linesep)

# 1 means get 1 random bytes
print(os.urandom(1))

# command line will stop at space, so use \"
# os.system(r'c:\"Program Files (x86)"\"Mozilla Firefox"\firefox.exe -url www.baidu.com')

# os.startfile is fine
# but seems unlike to pass arguments to execute -url www.baidu.com
# os.startfile(r'c:\Program Files (x86)\Mozilla Firefox\firefox.exe')

webbrowser.open('www.baidu.com')
