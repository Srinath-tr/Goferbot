from whatsapp import Client
import time
#import yowstack

phone_to = '918124766178'
#password='BIeu2r9O/APvK2HSKeWJHrtzEBo='
#password='yYVvYUQ5fmBBOXs5jHKrNGm0iTc='
client = Client(login='917092981752', password='BIeu2r9O/APvK2HSKeWJHrtzEBo=')
#receive = YowStack()
while True:
    msg = raw_input(">>> ")
    client.send_message(phone_to, msg)
    time.sleep(1)
    #rec = receive.receive(data)
    #print rec
    #print 'sending image'
    #client.send_media(phone_to, path='F://Camera//Sri.jpg')
    #print 'image sent'
    #break
    #client.receive_message(msg,phone_to)
