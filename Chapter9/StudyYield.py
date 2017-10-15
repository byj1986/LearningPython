# coding=UTF-8
import types
from collections import Iterable
from inspect import isgeneratorfunction


def fab(max):
    '''In a for/while loop, no need for handle StopIteration '''
    n, a, b = 0, 0, 1
    yield b
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print type(fab(2))

# 在for循环里，无需处理StopIteration异常，循环会正常结束。
for i in fab(5):
    print i

# print fab(5).next()

f = fab(15)
f2 = fab(10)
f3 = fab(5)
print id(f), id(f2), id(f3)

# 在这样的for循环中，还是要处理StopIteration异常
try:
    for i in range(1, 30):
        print f.next()
except StopIteration, e:
    pass
    # print e.message

f4 = fab(20)
print id(f4)

print id(fab(12)), id(fab(2))

print 'isgeneratorfunction'
print isgeneratorfunction(fab)
print isgeneratorfunction(f)

print 'isinstance of GeneratorType'
print isinstance(fab, types.GeneratorType)
print isinstance(f, types.GeneratorType)

print 'isinstance of Iterable'
print isinstance(fab, Iterable)
print isinstance(fab(5), Iterable)
