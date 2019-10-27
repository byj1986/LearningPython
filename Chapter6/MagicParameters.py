# def try_to_change(n):
#     n = 'Mr Bao'
#
#
# name = 'Mrs Bao'
#
# try_to_change(name)
#
# print(name)
#
#
# def change(n):
#     n[0] = 'Mr Bao'
#
#
# names = ['Mrs Bao', 'Mrs Bao2']
#
# change(names)
#
# print(names)

me = 'Magnus Lie Hetland'


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


storage = {}
init(storage)
store(storage, me)
# storage['first']['Magnus'] = [me]
# storage['middle']['Lie'] = [me]
# storage['last']['Hetland'] = [me]

my_sister = 'Anne Lie Hetland'
store(storage, my_sister)
# storage['first'].setdefault('Anne', []).append(my_sister)
# storage['middle'].setdefault('Lie', []).append(my_sister)
# storage['last'].setdefault('Hetland', []).append(my_sister)

print(storage)
print(storage['first']['Anne'])
print(storage['middle']['Lie'])

# init(mysister)

# print(storage['first']['Magnus'])

print(lookup(storage, 'middle', 'Lie'))

store(storage, 'Mr Gumby')


def hello_1(greeting, name):
    print('%s, %s!' % (greeting, name))


def hello_2(name, greeting):
    print('%s, %s!' % (name, greeting))


hello_1('Hello', 'World')

hello_2('World', 'Hello')

hello_2(greeting='Hello', name='World')
hello_2(greeting='World', name='Hello')
