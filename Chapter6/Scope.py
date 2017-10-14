x = 1

scope = vars()

print scope['x']

scope['x'] += 1

print scope['x']
print scope['x']

print x


def change_global():
    global x
    x += 1


change_global()

print x
