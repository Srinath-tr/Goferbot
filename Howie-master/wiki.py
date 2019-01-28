import wikipedia

wiki_search(query):
    p=wikipedia.page("query")
    print(p)
    print(p.url)
    print(p.title)
    content=p.content
    slash=content.find('/')
    result=content[:slash]
    content=content[slash+1:]
    slash=content.find('/')
    fstop=content.find('.')
    result=result+content[slash+2:fstop]
    return result
    #print(result)
