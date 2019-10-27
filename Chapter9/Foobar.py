class Foobar:
    def __init__(self):
        print('Foobar init')
        self.somevar = 42


f = Foobar()
print(f.somevar)


class A:
    def hello(self):
        print('Hello, I''m A')


class B(A):
    def hello(self):
        print('Hello, I''m B')


a = A()
a.hello()

b = B()
b.hello()
