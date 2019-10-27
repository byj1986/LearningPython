class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        print('before next', self.a, self.b)
        self.a, self.b = self.b, self.a + self.b
        print('after next', self.a, self.b)
        return self.a
        #
        # def __iter__(self):
        #     print('__iter__')
        #     return self


fibs = Fibs()


# print(type(range(10)))

# for i in range(10):
#     print(fibs.next())


class TestIter(object):
    value = 0

    def next(self):
        self.value += 1
        if self.value > 5:
            raise StopIteration
        return self.value

    def __iter__(self):
        print("__iter__")
        self.value += 1
        return self


# ti = TestIter()
# ti.next()
# ti.next()
# ti.next()

# StopIteration will not be raise out side in for iteration

ti = TestIter()
print(list(ti))

# print(ti.next())
# will get a StopIteration


# a = [1, 2, 3, 4]
# # print(type(a))
#
# it = iter(a)
# for i in range(a.__len__()):
#     print(it.next())
