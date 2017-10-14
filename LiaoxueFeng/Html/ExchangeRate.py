# -*-coding=UTF-8-*-
import urllib2

# 数据源
sourceHtml = r'http://www.boc.cn/sourcedb/whpj/'

response = urllib2.urlopen(sourceHtml)

html = response.read()

print html
