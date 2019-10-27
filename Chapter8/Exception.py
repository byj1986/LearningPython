import exceptions

try:
    print(1 / "Hello")

except (ZeroDivisionError, TypeError) as e:
    print('divid by zero')
    print(e.message)

# raise ValueError('aaa')

print(dir(exceptions))
