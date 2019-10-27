# Set

s = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(s)

a = set([1, 2, 3])
b = set([1, 4, 3])

print("a union b: ", a.union(b))
print("a | b ", a | b)
print

print("a intersection b: ", a.intersection(b))
print("a & b", a & b)
print

print("a difference b", a.difference(b))
print("a - b", a - b)
print

c = a & b
print(c.issubset(a), c.issubset(b))
print

print("a symmetric_difference b", a.symmetric_difference(b))
print("a ^ b", a ^ b)

# reduce set
mySets = []
for i in range(10):
    mySets.append(set(range(i, i + 5)))

print(mySets)
print(reduce(function=set.union, sequence=mySets))

# frozenset

a = set([1, 2])
b = set([2, 3])
a.add(frozenset(b))
print(a)

# heap
