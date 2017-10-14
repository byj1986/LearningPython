import math

fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print fibs

print callable(fibs)

print callable(math.sqrt)


def hello(name):
    print "Hello", name


hello("bao")


def fibs(nums):
    result = [0, 1]
    for i in range(nums):
        result.append(result[-2] + result[-1])
    return result


print fibs(10)


def square(num):
    """Calculates the square of the num"""
    return num * num


# print square(10)
print square.__doc__
