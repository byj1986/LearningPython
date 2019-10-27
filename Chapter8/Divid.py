# while True:
#     try:
#         x = float(input('please input first number: '))
#         y = float(input('please input second number: '))
#         print '%f/%f is %f' % (x, y, x / y)
#     except (ZeroDivisionError, TypeError, NameError, SyntaxError):
#         print "Invalid input. Please try it again"
#     else:
#         break

x = None
try:
    1 / x
except (ZeroDivisionError, TypeError) as e:
    print(e.message)
    pass
finally:
    del x
    print('Cleanup')
