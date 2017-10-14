print list('hello')

# print list(12345)

x = [1, 1, 1]
x[2] = 2
print x

names = ['alice', 'beth', 'cecil', 'earl']
names.extend(['delta', 'charlie'])
del names[2]
print names

name = list('Perl')
print name

print name[2:]

name[2:] = list('ar')
print name

numbers = [1, 5]
print numbers
numbers[1:1] = [2, 3, 4]
print numbers

# numbers=[1,2,3,4,5]

numbers[1:4] = []

print numbers

print ('-----------------------------------------')

sentence = ['to', 'be', 'or', 'not', 'to', 'be']
print sentence

print 'SSSSSSSSSSSSSSSS' + str(sentence[4])

if sentence[4] == 'not':
    print ('Equals')

print 'to: ' + str(sentence.count('to'))
print 'be: ' + str(sentence.count('be'))
print 'or: ' + str(sentence.count('or'))

print '' + str(sentence.index('or'))

# if [username, pwd] in database:
#    print 'Access granted'
if ['not'] in sentence:
    print sentence.index('not in sentence')
if ['net'] in sentence:
    print sentence.index('net in sentence')

print ('-----------------------------------------')

a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print a
