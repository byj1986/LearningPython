# open(r'C:\text\aaa.txt')

f = open('sometext.txt', 'w')
f.write('hello, ')
f.write('world!')
f.flush()
f.close()

f = open('sometext.txt', 'r')
print f.read(4)
print f.read()
f.close()
