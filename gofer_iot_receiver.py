import time
import datetime
import sys
from urllib2 import urlopen
import requests

url = "http://goferiot.16mb.com/get_command.txt"
flag=0
while True:
    data = urlopen(url).read()
    if flag==0:
        print data
        data1=data
        flag=1
    else:
        if not data==data1:
            print data
            data1=data
    time.sleep(1)
    
    
    
