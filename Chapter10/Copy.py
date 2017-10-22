import copy

# from copy import *

print copy

print type(copy)

print dir(copy)

print [n for n in dir(copy) if not n.startswith('_')]
# it's inside the copy.py file

print copy.__all__

# print copy.Error



# for n in copy.__all__:
#     print n

# help(copy)
