#!/usr/bin/python
import wikipedia

def wiki_search(query):
    print 'horas ya'
    p=wikipedia.page(query)
    print(p)
    print(p.title)
    print(p.url)
    print((p.content))
    print(p)
    
    #print('summary: '+p.summary + 'seri')
    
#
'''slash=content.find('/')
result=content[:slash]
content=content[slash+1:]
slash=content.find('/')'''#
#fstop=content.find('.')
#result=result+content[slash+2:fstop]
#content = content[:fstop]
#print content
#return content
#print(result)
#wiki_search('virat kohli')
#wiki_search("dhoni")
