from DecoratorCore import *


#
# def now():
#     print '2013-12-25'
#
# f = now
# f()
# print '----------------'
# now()
# print '----------------'
#
# print now.__name__
#
# print f.__name__
#
# print f == now
#
#
# @log
# def now():
#     print '2013-12-25'
#
#
# print '----------------'
# now()
#
# print '----------------'
#
@log
def now():
    # print('2013-12-25')
    DecoratorCore.hello()


now()


