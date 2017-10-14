print "factorial"


def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print factorial(5)


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return factorial_recursive(n - 1) * n


print factorial_recursive(5)

print "power"


def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


print "power", 3, 5, power(3, 5)


def power_recursive(x, n):
    if n == 1:
        return x
    else:
        return x * power(x, n - 1)


print "power", 3, 5, power_recursive(3, 5)


def func(x):
    return x.isalnum()


seq = ["foo", "x41", "?!", "****"]

print filter(func, seq)

"x41".isalnum()
