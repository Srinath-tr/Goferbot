import urllib2
import requests
import html2text
url='https://en.wikipedia.org/wiki/Python_(programming_language)'
html=urllib2.urlopen(url)
page=html.read()
#page=open('webContent.txt','r')
#r=requests.get(url)
#print(r.title)
#page=r.content

#print(page)
#page=page.decode('utf-8')
page=page.decode('ascii','ignore')
#html2text.html2text(page)
page=html2text.html2text(page)
print(unicode.lower(page))
