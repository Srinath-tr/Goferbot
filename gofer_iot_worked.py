import time
import datetime
import sys
from urllib2 import urlopen
import requests

command = "lights on"
post_cmd = "http://goferiot.16mb.com/default.php"
form_data={
    'text_box':command,
    'search-submit':'submit',
    }
requests.post(post_cmd, data=form_data)

url = "http://goferiot.16mb.com/get_command.txt"
data = urlopen(url).read()
print data

