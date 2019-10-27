from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1


class Employee:
    name = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print('Hello' + self.name)

    @staticmethod
    def printMethod():
        print("Helloworld")


class Manager(Employee):
    def sayHello(self):
        print("Hello from Manager: " + self.name)


class Person(Employee):
    gender = Gender.Male

    def __init__(self):
        self.gender = Gender.Male

    def __init__(self, gender):
        self.gender = gender
