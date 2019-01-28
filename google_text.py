# -*- coding: cp1252 -*-
from google import search
import urllib2
import html2text
import TextSearch
import wikipedia
import Amazon_Search

page=u' '
flag=''
avail=''
pf=0

def price_search(GS):
    pf=0
    cat=0
    subject = TextSearch.get_subject(GS)
    GS_A = GS + ' in amazon'
    #try:
    print('amazon subject: ' + GS_A)
    try:
        for url in search(GS_A, start=0,num=3,stop=3):
            print(url)
            info = Amazon_Search.AmazonParser(url)
            #print(info)
            price = info['SALE_PRICE']
            if str(price) == 'None':
                continue
            category = info['CATEGORY']
            name = info['NAME']
            #print(category)
            if category == 'None':
                category = 'none'
            else:
                while cat>=0:
                    if ">" in category:
                        category = category[cat+1:]
                        cat = category.find('>')
                        #print('cat: ' + str(cat))
                    else:
                        break
            #print(info)
            avail = info['AVAILABILITY']
            print('the price of ' + name +' in amazon is ' + str(price) + ' and is ' + str(avail) + '.')
            print('the category of the product is: ' + str(category))
            pf = 1
            break
        if pf==0:
            print 'price not found or unavailable in amazon'
    except:
        print 'connection error occurred'
        return -1
    return pf

def g_search(GS):
    try:
        for url in search(GS,start=1,num=10,stop=11):
            print(url)
            try:
                html=urllib2.urlopen(url)
            except:
                continue
            #r=requests.get(url)
            page=html.read()
            page=page.decode('ascii','ignore')
            #page=page.encode('ascii','ignore')
            page = html2text.html2text(page)
            #page=page.decode('utf-8')
            print(page)
            print 'page fetched'
            try:
                page=unicode.lower(page)
            except:
                try:
                    page=str.lower(page)
                except:
                    print 'text conversion error'
            flag = TextSearch.Tsearch(page,GS)
            if flag == '0':
                break
            elif flag == '-1':
                continue
    except:
        print 'connection error occurred'
        
while True:
    pf=0
    cat=0
    GS=raw_input("Google search: ")
    if 'price' in GS:
        pflg = price_search(GS)
        if pflg == 0:
            g_search(GS)
        elif pflg == -1:
            print 'check your internet connection'
    else:
        g_search(GS)
