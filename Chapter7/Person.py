__metaclass__ = type


class Person:
    print("class Person is defined")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello world", self.name)


foo = Person()
foo.set_name("B")
bar = Person()
bar.set_name("A")

foo.greet()
bar.greet()
