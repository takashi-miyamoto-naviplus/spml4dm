#coding:utf-8

import sys
import urllib2
from bs4 import BeautifulSoup as BS

url = u'http://ja.wikipedia.org/wiki/' + sys.argv[1]
html = urllib2.build_opener().open(url).read()
soup = BS(html)
text = soup.findAll("p")
for sub in text:
    print sub.get_text()

