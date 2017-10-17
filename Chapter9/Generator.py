nested = [[1, 2], [3, 4], [5]]
print nested


def flatten(n):
    for sublist in n:
        for element in sublist:
            yield element


fla = flatten(nested)
print type(fla)

for num in fla:
    print num


# fla.next()

def flatten2(n):
    try:
        for sublist in n:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield n


print 'flatten2'
fla2 = flatten2(nested)
for num in fla2:
    print num


def flatten3(n):
    '''If n is a string, will raise a TypeError and pass'''
    try:
        try:
            n + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in n:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield n


fla3 = flatten3(['abcd', ['ef', ['g']]])

# print fla3.next()
for a in fla3:
    print a


def simple_generator():
    yield 1


print simple_generator()
print simple_generator


def repeater(val):
    '''below print just executed once'''
    '''cause after first execution of next(), it execute statement after yield'''
    print 'repeater'
    while True:
        print 'repeater while'
        new = (yield val)
        if new is not None: val = new


r = repeater(42)
print r.next()
print r.send("Hello world")
print r.send("Hello world")

r.close()
# can't send or next after close
# r.send("Hello world2")

del r
print r


def flatten4(n):
    '''method without yield, pretty same as flatten3 but it will store temporary result in memory'''
    result = []
    try:
        try:
            n + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in n:
            for element in flatten4(sublist):
                result.append(element)
    except TypeError:
        result.append(element)
    return result
