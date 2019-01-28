# -*- coding: cp1252 -*-
import string
import time
import sys
import re

'''content=open("detail.txt","r")
content=content.read()
content=str.lower(content)
#print(" "+content)'''
query='what is', 'define', 'about', 'definition'
val='price of', 'the price of', 'the prise of', 'prise of', 'the cost of', 'cost of','the rate of', 'rate of'
person='who is','who was'

def get_subject(subject):
    #subject=str.lower(raw_input("enter your query: "))
    v=''
    result=''
    subject=str.lower(subject)
    if subject=="exit" or subject=="quit":
        exit()
    for q in query:
        if q in subject:
            #print(q)
            subject=subject[len(q)+1:]
            break
    if subject=='':
        print("subject: No subject")
        return
    for v in val:
        if v in subject:
            #ad = 'price'
            pos=subject.find(v)
            subject = subject[pos+len(v):]
            print("subject in price: "+subject)
            return subject

def person_search(content,subject):
    symbols = set('#$.<>*+{}[]%^!?\//')
    iswas = 'is','was'
    s=''
    fstop=-1
    flag=0
    subject=subject+' '
    while flag==0:
            sub=content.find(subject)
            #print("sub: "+str(sub))
            #time.sleep(2)
            if(sub>=0):
                for iw in iswas:
                    ispos=(content[sub:].find(' is '))
                    break
                if ispos>0:
                    #print(sub+ispos)
                    for s in symbols:
                    #print(s)
                        fstop=(content[sub:sub+ispos].find(s))
                        if fstop>0:
                            break
                else:
                    print 'data not found'
                    #break
                    return '-1'
                
                if(fstop>0):
                    content=content[sub+fstop:]
                    #time.sleep(2)
                    continue
                if(ispos>0):
                    end=content[sub+ispos:].find(".")
                    if(end>0):
                        context=content[sub:sub+ispos+end]
                        #print 'your required data is:'
                        #print(context)
                        flag=1
                        return context
                        #break
                    else:
                        content=content[sub+ispos+end:]
                        flag=0
                        continue
            else:
                print 'data not found1'
                return '-1'
                #break

def query_search(content,subject):
    symbols = set('#$.<>*+{}[]%^!?\//')
    #iswas = 'is','was'
    s=''
    fstop=-1
    flag=0
    subject=subject+' '
    while flag==0:
            sub=content.find(subject)
            #print("sub: "+str(sub))
            #time.sleep(2)
            if(sub>=0):
                #for iw in iswas:
                ispos=(content[sub:].find(' is '))
                if ispos>0:
                    #print(sub+ispos)
                    for s in symbols:
                    #print(s)
                        fstop=(content[sub:sub+ispos].find(s))
                        if fstop>0:
                            break
                else:
                    print 'data not found'
                    #break
                    return '-1'
                
                if(fstop>0):
                    content=content[sub+fstop:]
                    #time.sleep(2)
                    continue
                if(ispos>0):
                    end=content[sub+ispos:].find(".")
                    if(end>0):
                        context=content[sub:sub+ispos+end]
                        #print 'your required data is:'
                        #print(context)
                        flag=1
                        return context
                        #break
                    else:
                        content=content[sub+ispos+end:]
                        flag=0
                        continue
            else:
                print 'data not found1'
                return '-1'
                #break

def price_search(content,subject):
    symbols = set('#$.<>*+{}[]%^!?\//')
    s=''
    fstop=-1
    flag=0
    subject=subject+' '
    sub=content.find(subject)
    price=''
    tag=0
    #print("sub: "+str(sub))
    #time.sleep(2)
    if(sub>=0):
            tag=(content.find(" price "))
            print('tag: ' + str(tag))
            if tag>0:
                #while flag==0:
                fstop=content[tag:].find('. ')
                print('fstop: ' + str(tag+fstop))
                if(fstop>=0):
                    price = re.findall('[rs.]?[Rs.]?\d+[\,]?\d+[\.]?\d*',content[tag:])
                    if not price:
                        #content=content[tag+fstop:]
                        #print(content)
                        print 'empty'
                        #tag=0
                        #continue
                    else:
                        #print(content[tag:tag+fstop])
                        print(price)
                        print('price is: ' + str(price[0]))
                        flag=1
                        return price[0]
            else:
                print 'no price found'
                return '-1'
    else:
        print 'no matching results found'
        return '-1'
    
def Tsearch(content,subject):
    #subject=str.lower(raw_input("enter your query: "))
    v=''
    result=''
    try:
        content=unicode.lower(content)
    except:
        try:
            content=str.lower(content)
        except:
            print 'conversion error in Tsearch'
    subject=str.lower(subject)
    if subject=="exit" or subject=="quit":
        exit()
        
    for q in query:
        if q in subject:
            #print(q)
            subject=subject[len(q)+1:]
            break
        
    for p in person:
        if p in subject:
            subject=subject[len(p)+1:]
            print('subject: ' + subject)
            result = person_search(content,subject)
            if result == '-1':
                return '-1'
            else:
                print("your required data is: " + result)
                return '0'
            
    if subject=='':
        print("subject: No subject")
        return
    
    for v in val:
        if v in subject:
            #ad = 'price'
            pos=subject.find(v)
            subject = subject[pos+len(v):]
            print("subject in price: "+subject)
            result = price_search(content,subject)
            if result == '-1':
                return '-1'
            else:
                print("your required data is: " + result)
                return '0'
            #break
    else:
        print("subject: "+subject)
        result = query_search(content,subject)
        if result=='-1':
            return '-1'
        else:
            print("your required data is: " + result)
            return '0'
        
        
                        
