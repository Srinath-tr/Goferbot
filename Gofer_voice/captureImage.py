import cv2
import sys
import os
import time
#import speech_recognition as sr
#import pyttsx
#import speech
#from wpy import sendimage

def capture():
    #count = sys.argv[1:]
    img_list = os.listdir("capturedImages")
    count = len(img_list) + 1
    video_capture = cv2.VideoCapture(0)
    time.sleep(1)
    ret, frame = video_capture.read()

    ImageFileName = "G:\\Python27\\Gofer_voice\\capturedImages\\img" + str(count) + ".jpg"
    cv2.imwrite(ImageFileName, frame)

    #Display the image 
    cv2.imshow('Result',frame)
    print 'image taken...'
    #speech.say('image taken')
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
    #sendimage('917845594613',ImageFileName)

#capture()
