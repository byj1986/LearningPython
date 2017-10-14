import exceptions

try:
    print 1 / "Hello"

except (ZeroDivisionError, TypeError), e:
    print 'divid by zero'
    print e.message

# raise ValueError('aaa')

print dir(exceptions)
