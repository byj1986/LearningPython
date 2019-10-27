format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)

# Print Pi with 5 decimals
format = "Pi with three decimals: %.5f"
from math import pi

print(pi)

print(format % pi)

from string import Template

# substitute $x
s = Template('$x, glorious $x!')
s = s.substitute(x='slurm')
print(s)

# double $$ for $
s = Template("Make $$ selling $x!")
s = s.substitute(x='slurm')
print(s)

s = Template('Fox $jumps over a $tree')
d = {}
d['jumps'] = 'jumps'
d['tree'] = 'trese'
s = s.substitute(d)
print(s)

print('%s plus %s equals %s' % (1, 1, 2))

# print('%s plus %s equals %s' % 1, 1, 2)

# pricelist

# print(string.letters)

# join and split
seq = ['', 'usr', 'bin', 'env']
print('\\'.join(seq))

print

# width = 60
width = input('enter width: ')
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print('=' * width)
print(header_format % (item_width, 'Item', price_width, 'Price'))
print('-' * width)
print(format % (item_width, 'Apples', price_width, 0.4))
print(format % (item_width, 'Pears', price_width, 0.5))
print(format % (item_width, 'Cantaloupes', price_width, 1.92))
print(format % (item_width, 'Dried Apricots', price_width, 8))
print(format % (item_width, 'Prunes', price_width, 12))
