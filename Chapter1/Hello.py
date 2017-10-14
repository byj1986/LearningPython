print('Hello world')

import Employee

me = Employee.Employee("yinjun", 32)

print type(me)

me.sayHello()

Employee.Employee.printMethod()

print Employee.Employee.__doc__

print Employee.Employee.__dict__
