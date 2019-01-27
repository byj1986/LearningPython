# -*- coding: utf-8 -*-

# 把@log放到now()函数的定义处，相当于执行了语句：

# now = log(now)

# 似乎装饰器的名称必须唯一，不能重载
def log(func):
    print('call %s():' % func.__name__)

    def wrapper(*args, **kw):
        return func(*args, **kw)

    return wrapper


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func

        return wrapper

    return decorator


def log3(text, func):
    def wrapper(*args, **kw):
        print('%s %s():' % (text, func.__name__))
        return func

    return wrapper


def hello():
    print("123444")
