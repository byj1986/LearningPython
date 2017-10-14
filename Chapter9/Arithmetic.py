def checkindex(key):
    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkindex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        checkindex(key)
        self.changed[key] = value


a = ArithmeticSequence(1, 2)
print a[4]

a[4] = 2
print a[4]

print a[5]

# del a[4]
