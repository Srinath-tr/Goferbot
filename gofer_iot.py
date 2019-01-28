
from urllib2 import urlopen
import requests

post_cmd = "http://goferiot.16mb.com/default.php"

while True:
    command = raw_input(">>> ")
    form_data={
        'text_box':command,
        'search-submit':'submit',
        }
    requests.post(post_cmd, data=form_data)

    url = "http://goferiot.16mb.com/get_command.txt"
    data = urlopen(url).read()
    print data

