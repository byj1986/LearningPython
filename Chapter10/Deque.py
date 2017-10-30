# coding=UTF=8
# Deque Double-ended queue 双端队列
from collections import deque

q = deque(range(5))
print q
q.append(5)
print q
q.appendleft(6)
print q

print q.pop()

print q.popleft()

print
print q
q.rotate(3)
print q

q.rotate(-1)
print q
