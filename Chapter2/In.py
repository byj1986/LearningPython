permissions = 'rw'
print 'w' in permissions
print 'x' in permissions

users = ['mlh', 'foo', 'bar']

print raw_input('User: ') in users

subject = '$$$ Get rich now!!! $$$'

print '$$$' in subject

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['johns', '9843'],
    ['bao', 'everything'],
]

username = raw_input('User name: ')
pwd = raw_input('Pwd: ')
if [username, pwd] in database:
    print 'Access granted'
