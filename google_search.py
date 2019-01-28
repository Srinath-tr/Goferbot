from google import search
#import urllib
while True:
    a=raw_input("Google search: ")
    for url in search(a,start=1,num=10,stop=11):
        print(url)
