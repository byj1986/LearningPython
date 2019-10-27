# while looping

# name = ''
# while not name:
#     name = raw_input('Please input your name: ')
#
# print('Hello, %s' % name)

# for looping
# words = ['this', 'is', 'an', 'ex', 'parrot']
# for word in words:
#     print(word)

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, ':', d[key])

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 60]

persons = zip(names, ages)

print(persons)

for name, age in persons:
    print(name + ''''s age is ''' + str(age))
