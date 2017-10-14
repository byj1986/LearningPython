__metaclass__ = type


class MyClass:
    def smeth():
        print 'This is a static method'

    smeth = staticmethod(smeth)

    def cmeth(cls):
        print 'This is a class method of', cls

    cmeth = classmethod(cmeth)


MyClass.smeth()
MyClass.cmeth()
my = MyClass()
my.cmeth()


class MyClass2:
    @staticmethod
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls


MyClass2.smeth()
MyClass2.cmeth()
my2 = MyClass2()
my2.cmeth()
