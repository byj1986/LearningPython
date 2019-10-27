import re
import urllib

url = 'http://www.python.org'
webpage = urllib.urlopen(url)
text = webpage.read()
# print(webpage)
# print(text)

m = re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
print(m.group(1))

urllib.urlretrieve(url, "python.html")

urllib.urlcleanup()

# http://www.w3school.com.cn/tags/html_ref_urlencode.html
# refer the html for more information about html url coding/encoding
word = urllib.quote(' ')
print(word)

word = urllib.unquote('%3d')
print(word)
