import speech
import sys

data = sys.argv[1:]
#data = 'hello'
print data
speech.say(data)
