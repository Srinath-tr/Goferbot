from chatterbot import ChatBot
import re
import random

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
print("Hi, Welcome! How are you doing?")

while(True):
    statement = str(raw_input("> "))
    print(chatbot.get_response(statement))
    #print(res)
    #res=chatbot.get_response(res)
    if statement=="quit" or statement=="bye":
        break
