def add_end(L=[]):
    print 'id of L is:', id(L), 'L type:', type(L)
    print 'id of [] is:', id([]), '[] type:', type(L)
    L.append('END')
    return L


def add_end2(L=None):
    print 'id of L is:', id(L), 'L type:', type(L)
    print 'id of [] is:', id([]), '[] type:', type(L)
    if L is None:
        L = []
    L.append('END')
    return L


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def calc_nor(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
