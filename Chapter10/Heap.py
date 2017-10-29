from heapq import *
from random import shuffle

'''aaabbb'''
data = range(100)
shuffle(data)
# print data
heap = []
for n in data:
    heappush(heap, n)

# print heap
# heappush(heap, 0.5)
# print heap

index = 0
print heap
# print heap.__len__()
# while index < heap.__len__():
#     ele = heap[index]
#     halfPos = index / 2
#     halfElement = heap[halfPos]
#     print "index: %d, half position: %d, element %d, HalfPosition %d, " % (index, halfPos, ele, halfElement)
#     if (ele < halfElement):
#         raise AssertionError('not match heap definition')
#     index += 1
