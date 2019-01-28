from wikiapi import WikiApi

sub = "sachin tendulkar"
wiki = WikiApi()
wiki = WikiApi({'locale':'en'})
page = wiki.get_article(sub)
print(page.content)
