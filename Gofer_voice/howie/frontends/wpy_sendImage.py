from whatsapp import Client
import time
import os
#import sys

client = Client(login='917092981752', password='yYVvYUQ5fmBBOXs5jHKrNGm0iTc=')
#receive = YowStack()

def sendimage(phone_to, path):
    client.send_media(phone_to, path)
    print 'image sent'

img_list = os.listdir(r'G:\Python27\Gofer_voice\capturedImages')
count = len(img_list)
print count
ImageFileName = 'G:\Python27\Gofer_voice\capturedImages\img' + str(count) + '.jpg'
print ImageFileName
phone_to = '918124766178'
sendimage(phone_to,ImageFileName)

