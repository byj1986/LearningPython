permissions = 'rw'
print('w' in permissions)
print('x' in permissions)

users = ['mlh', 'foo', 'bar']

print(input('User: ') in users)

subject = '$$$ Get rich now!!! $$$'

print('$$$' in subject)

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['johns', '9843'],
    ['bao', 'everything'],
]

username = input('User name: ')
pwd = input('Pwd: ')
if [username, pwd] in database:
    print('Access granted')
