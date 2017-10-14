import cPickle

d = dict(name='Bob', age=20, score=88)

print cPickle.dumps(d)
f = open('dump.txt', 'wb')
cPickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
ob = cPickle.load(f)
print ob

print '--------------json------------------'
import json

print json.dumps(d)

f2 = open('dump.txt', 'rb')
print json.load(f2)
