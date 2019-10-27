class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height


r = Rectangle()

r.width = 100
r.height = 150
print(r.getSize())

r.setSize((10, 20))
print(r.width, r.height)


class Rectangle2(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)
    readableSize = property(getSize)


print('Rectangle2')
r2 = Rectangle2()
r2.width = 20
r2.height = 30
print(r2.size)
r2.size = 150, 100
print(r2.width, r2.height)
print(r2.readableSize)


# unable to set value
# r2.readableSize = 10, 20

class Rectangle3(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        print('__setattr__', key, value)
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print('__getattr__', item)
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError


print('Rectangle3')
rect3 = Rectangle3()
rect3.width = 20
rect3.height = 30

print(rect3.width)
print(rect3.size)
print(rect3.height)
print(rect3.aa)
