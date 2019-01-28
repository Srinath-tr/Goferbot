import speech_recognition as sr
import pyttsx
from chatterbot import ChatBot
import re
import random

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
