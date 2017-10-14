people = {
    'Alice': {'phone': 2341, 'addr': 'Foo drive 23'},
    'Beth': {'phone': 9102, 'addr': 'Bar street 23'},
    'Cecil': {'phone': 3158, 'addr': 'Baz avenue 23'},
}

# print people
print "Cecil's phone number is %(Cecil)s." % people

# request = raw_input('Phone (p) or address (a): ')

req = 'phone'

# if (request == 'p'):
#     req = 'phone'
# elif (request == 'a'):
#     req = 'addr'
# else:
#     raise ValueError('input value is not \'p\' or \'a\'')

name = 'Beth'

if name in people:
    print type(people[name])
    print "%s's %s is %s" % (name, req, people[name][req])

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
x['username'] = 'mlh'
x['machines'].remove('baz')

print 'x: ', x
print 'y: ', y

print x.get('ipaddress', '127.0.0.1')
