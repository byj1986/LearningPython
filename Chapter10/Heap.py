from heapq import *
from random import shuffle

data = range(10)
shuffle(data)
# print data
heap = []
for n in data:
    heappush(heap, n)

print heap
print heappop(heap)
print heappop(heap)
print heap
heapify(heap)
print heap
# higher performance than heappop and heappush
heapreplace(heap, 0.5)
print heap

print heappop(heap)
heappush(heap, 10)
# heapreplace(heap, 10)
print heap

print nlargest(3, heap)

print nsmallest(3, heap)
# print heap
# heappush(heap, 0.5)
# print heap
#
# index = 0
# print heap
# print heap.__len__()
# while index < heap.__len__():
#     ele = heap[index]
#     halfPos = index / 2
#     halfElement = heap[halfPos]
#     print "index: %d, half position: %d, element %d, HalfPosition %d, " % (index, halfPos, ele, halfElement)
#     if (ele < halfElement):
#         raise AssertionError('not match heap definition')
#     index += 1
