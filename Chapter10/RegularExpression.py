import re

some_text = 'alpha, beta,,,,gamma delta'

print re.split('[, ]+', some_text)

print re.split('[, ]+', some_text, maxsplit=2)

print re.split('[, ]+', some_text, maxsplit=1)

pattern = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
print re.findall(pattern, text)

# if not use\ before -, - will be consider like A-Z
pattern = r'[.?\-",]+'
print re.findall(pattern, text)

pattern = '{name}'
text = 'Hello {name}'
print re.sub(pattern, "Mr Bao", text)

print text

print re.escape('www.python.org')

print re.escape('But where is the ambiguity')

text = 'There (was a (wee) (cooper)) who (lived in Fyfe)'

print re.match('\(\.*', text)

# r = re.match('\(\.\+\)', text)
# print r.groups()
# print r.group(0)

# print r.group(1)

s = 'www.python.org'
r = re.match(r'www\.(.*)\..{3}', s)
# group(0) return itself
print r.groups()
print r.group(0)
print r.group(1)
print r.start(1)
print r.end(1)

print s.index('p')
# print s.index('n')

# print r.group()

emphasis_pattern = r'\*([^\*]+)\*'
emphasis_pattern2 = re.compile(
    r'''
\*      # Beginning emphasis tag -- an asterisk
(       # Begin group for capturing phrase
[^\\*]+  # Capture anything except asterisks 
)       # End group
\*      # Ending emphasis tag
'''
    , re.VERBOSE
)

print emphasis_pattern == emphasis_pattern2.pattern
print re.sub(emphasis_pattern2, r'<em>\1</em>', 'Hello, *world*!')
