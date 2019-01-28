from whatsapp import Client
import time
#import yowstack
#from layer import echolayer
phone_to = '918124766178'

client = Client(login='917092981752', password='yYVvYUQ5fmBBOXs5jHKrNGm0iTc=')
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
    #rec = Echolayer.Onreceipt(msg,phone_to)
    #print rec
    
