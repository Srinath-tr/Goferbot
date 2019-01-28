import subprocess
#import speech
import speech_recognition as sr
import random
import sys
import time
import pyttsx
import re

r = sr.Recognizer()
m = sr.Microphone()

while True:
    print ">>input: "
    with m as source: audio = r.listen(source)
    print("Got it! Now to recognize it...")
    #try:
    # recognize speech using Google Speech Recognition
    value = r.recognize_google(audio)
    # we need some special handling here to correctly print unicode characters to standard output
    if str is bytes:
        result = format(value).encode("utf-8")
        result = str.lower(result)
        print(result)
        subprocess.Popen(['python','speakme.py',result])
        result = ''
    #except:
    #    print 'no input'
        #speech.say('check your internet connection')
    #    continue
