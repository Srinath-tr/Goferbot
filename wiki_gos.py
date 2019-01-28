#!/usr/bin/python
import wiki

#wikiquery="dhoni"
#wiki.wiki_search(wikiquery)

qn = 'what is', 'who is', 'who was', 'what are', 'who are', 'tell me about'
query = "who is dhoni"
wikiquery=""
flag=0
#googler = Googlismer()
print 'query: ' + queryx
#try:
for q in qn:
    if q in query:
        wikiquery = query[len(q):]
        flag=1
        break
                #print 'gos'
                #print wikiquery
                #wiki.wiki_search(wikiquery)
                #p=wikipedia.page(wikiquery)
                #print('url: ' + p.url)
                #print(p.content)
                #print 'kai horyp'
                #break
                        #print p.title
                        #content = p.content
                        #print content
                        #fstop = content.find('.')
                        #response = content[0:fstop]
                        #response = wiki.wiki_search(query_wiki)
                        #print response
#print(p.title)
#print(p.url)
        #print(p.summary)
        
        #except:
        #        print 'googlism'
        #        googler = Googlismer()
        #        response = googler.respondTo(query)
        #response = googler.respondTo(query)
        #print response
if flag==1:
    wiki.wiki_search(wikiquery)
else:
    'michh'
