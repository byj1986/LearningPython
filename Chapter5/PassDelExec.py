from math import sqrt

# pass in an empty if else branch
age = 50
if 0 < age < 100:
    pass
else:
    print 'age is not valid'

scoundrel = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin = scoundrel
del scoundrel
# print scoundrel
print robin
# just delete scoundrel, not the dict, so print robin is still valid

# exec

exec "print 'Hello world'"

scope = {}
print len(scope)
exec "sqrt = 1" in scope
print sqrt(4)
print scope['sqrt']
print len(scope)
print scope.keys()

# eval
print eval(raw_input("Enter an arithmetic expression: "))
