# -*-coding=UTF-8-*-
import re

# s = 'ABC\\-001'  # Python的字符串'ABC\-001'
pattern = r'^\d{3}\-\d{3,8}$'
s = '010-12345'
match = re.match(pattern, s)
print match
s = s.replace('-', ' ')
match = re.match(pattern, s)
print match

s = 'a b  c'

match = re.split(r'\s+', s)
print match
