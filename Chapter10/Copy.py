import copy
import pprint
import sys

# from copy import *

print(copy)

print(type(copy))

print(dir(copy))

print([n for n in dir(copy) if not n.startswith('_')])
# it's inside the copy.py file

print(copy.__all__)

# print(copy.Error

# for n in copy.__all__:
#     print(n

# help(copy)

print(copy.copy.__doc__)

print(range.__doc__)

print(copy.__file__)

if __name__ == '__main__':
    pprint.pprint(sys.modules)
    pprint.pprint(sys.argv)
    pprint.pprint(sys.path)
    pprint.pprint(sys.platform)
    pprint.pprint(sys.stdin)
    pprint.pprint(sys.stdout)
    pprint.pprint(sys.stderr)
