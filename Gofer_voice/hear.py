import speech_recognition as sr
import sys
import time
import speech

r = sr.Recognizer()
m = sr.Microphone()

def hear():
    while True:
        print '>>input: '
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:
                data = format(value).encode("utf-8")
                data = str.lower(data)
                print data
                break
        except:
            print 'no input'
            continue

    return data

#h = hear()
#print h
