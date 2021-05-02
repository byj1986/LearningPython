# -*- coding: utf-8 -*-
# f=lambda x: x+1
# result = f(f(1))
# print(result)


# def test(ls=[]):
#     ls.append(1)
#     return ls


# a = test()
# b = test()
# print(a, b)

# 1 isNum

# def isNum(text: str) -> bool:
#     return isinstance(text, complex) or isinstance(text, int) or isinstance(text, float)


# print(isNum(2+3j))
# print(isNum(3))
# print(isNum(-5.4))
# print(isNum('abc'))

# 2 isPrime
# import math


# def isPrime(number: int) -> bool:
#     sqrt_number = int(math.sqrt(number))+1
#     for i in range(2, sqrt_number):
#         if number % i == 0:
#             return False
#     return True


# for i in range(3, 10):
#     print(f'{i} is prime: {isPrime(i)}')
# print(isPrime(20))
# print(isPrime(17))
# print(isPrime(13))
# print(isPrime(11))
# print(isPrime(11))

# 5 fibonacci
# 0、1、1、2、3、5、8、13、21、34
# def getFibonacci(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return getFibonacci(n-1)+getFibonacci(n-2)


# print(getFibonacci(20))
