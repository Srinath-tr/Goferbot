import time
import datetime
import sys
from urllib2 import urlopen
import requests
from Arduino import Arduino
#import RPi.GPIO as GPIO

'''GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)'''

board = Arduino('9600') #plugged in via USB, serial com at rate 9600
board.pinMode(8, "OUTPUT")
board.pinMode(9, "OUTPUT")

url="http://goferiot.16mb.com/get_command.txt"
flag=0
iot = 'lights on','lights off','lights of','light on','light of','switch on the light','switch off the light','switch off light','switch on the fan','switch on fan','switch off the fan','switch of the light','switch of the fan'
light_on = 'lights on','light on','switch on the light',
light_off = 'lights off','light of','switch of the light','switch off the light'
fan_on ='switch on the fan','switch on fan'
fan_off = 'switch of the fan','switch off the fan'

while True:
    data = urlopen(url).read()
    if flag == 0:
        print data
        if 'light' in data:
            if 'on' in data:
                print 'light on1'
                #GPIO.output(26,GPIO.HIGH)
                board.digitalWrite(8, "HIGH")
            elif 'off' in data:
                print 'light off1'
                #GPIO.output(26,GPIO.LOW)
                board.digitalWrite(8, "LOW")
        elif 'fan' in data:
            if 'on' in data:
                print 'fan on1'
                #GPIO.output(13,GPIO.HIGH)
                board.digitalWrite(9, "HIGH")
            elif 'off' in data:
                print 'fan off1'
                #GPIO.output(13,GPIO.LOW)
                board.digitalWrite(9, "LOW")
        else:
            print 'invalid input'
        data1 = data
        flag = 1
    else:
        if not data == data1:
            print data
            if 'light' in data:
                if 'on' in data:
                    print 'light on1'
                    #GPIO.output(26,GPIO.HIGH)
                    board.digitalWrite(8, "HIGH")
                elif 'off' in data:
                    print 'light off1'
                    #GPIO.output(26,GPIO.LOW)
                    board.digitalWrite(8, "LOW")
            elif 'fan' in data:
                if 'on' in data:
                    print 'fan on1'
                    #GPIO.output(13,GPIO.HIGH)
                    board.digitalWrite(9, "HIGH")
                elif 'off' in data:
                    print 'fan off1'
                    #GPIO.output(13,GPIO.LOW)
                    board.digitalWrite(9, "LOW")
            else:
                print 'invalid input'
            data1 = data
    time.sleep(1)
