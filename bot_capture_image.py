import speech_recognition as sr
import pyttsx
from chatterbot import ChatBot
import re
import random
import cv2
import sys

def img_capture():

    face_cascade = cv2.CascadeClassifier('E:\\OpenCv_new\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('E:\\OpenCv_new\\opencv\\sources\\data\\haarcascades\\haarcascade_eye.xml')
    count=0
    video_capture = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Resize Image 
        minisize = (frame.shape[1],frame.shape[0])
        miniframe = cv2.resize(frame, minisize)
      
        # Store detected frames in variable name faces
        faces =  face_cascade.detectMultiScale(miniframe)

        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255))
            #Save just the rectangle faces in SubRecFaces
            sub_face = frame[y:y+h, x:x+w]
            FaceFileName = "G:\\Python27\\faces\\gos\\img" + str(count) + ".jpg"
            count=count+1
            cv2.imwrite(FaceFileName, sub_face)
            #Display the image 
            cv2.imshow('Result',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if count==25:
            speak("Image stored in database.")
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
        speech_engine.say(text)
        speech_engine.runAndWait()

r = sr.Recognizer()
m = sr.Microphone()

try:
    #print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("Hi, Welcome! How are you doing?")
    speak("Hi, Welcome! How are you doing?")
    while True:
        print("Say something!")
        #speak("say something")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:
                    result = format(value).encode("utf-8")
                    print(result)
                    if(result in "Take make me a picture pictures"):
                        img_capture()
                    statement=chatbot.get_response(result)
                    speak(statement)
                    print(statement)
                    #if(result in word):
                    #        print(result)
                    #        speak("how are you buddy")
                    #else:
                    #        print(result)
                    #        speak("sorry. didn't hear you")
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
