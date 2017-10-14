# append
lst = [1, 2, 3]
lst.append(4)
print lst
print ('------------append------------')

sentence = ['to', 'be', 'or', 'not', 'to', 'be']
print sentence

if sentence[4] == 'not':
    print ('Equals')

print 'to: ' + str(sentence.count('to'))
print 'be: ' + str(sentence.count('be'))
print 'or: ' + str(sentence.count('or'))
print ('------------count------------')

a = [1, 2, 3]
b = [4.5, 6]
a.append(b)
print a
print ('------------extend------------')
c = [1, 2, 3]
d = [4, 5, 6]
c = c + d
print c
print ('------------plus------------')

print '' + str(sentence.index('or'))
print ('------------index------------')
sentence.insert(0, 'Test')
print sentence
print ('------------insert------------')

x = [1, 2, 3, 4, 5, 6]
print 'Popped ' + str(x.pop(1))
print x

x.append(x.pop())
print x
print ('------------pop------------')

x.reverse()
print x
print ('------------reverse------------')

x = [4, 6, 2, 1, 7, 9]

# y = x.sort()
# print y
y = x[:]  # Copy list
y.sort()
print y
print x
print ('------------sort------------')

strs = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
strs.sort(key=len)
print strs
print ('------------sort by len------------')
