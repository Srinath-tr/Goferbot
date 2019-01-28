from whatsapp import Client
import time

#phone_to = '918124766178'

client = Client(login='917092981752', password='yYVvYUQ5fmBBOXs5jHKrNGm0iTc=')
#receive = YowStack()
def sendmessage(phone_to,msg):
    #msg = raw_input(">>> ")
    client.send_message(phone_to, msg)

def sendimage(phone_to, path):
    client.send_media(phone_to, path)
    print 'image sent'
    
    
#sendmessage('918124766178','hello')
