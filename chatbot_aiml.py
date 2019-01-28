import aiml
import os

kernel = aiml.Kernel()

'''if os.path.isfile("G:\\Python27\\Lib\\site-packages\\aiml\\standard\\bot_brain.brn"):
    print 'hai'
    kernel.bootstrap(brainFile = "G:\\Python27\\Lib\\site-packages\\aiml\\standard\\bot_brain.brn")
else:'''
kernel.bootstrap(learnFiles = "G:\\Python27\\Lib\\site-packages\\aiml\\standard\\startup.xml", commands = "load aiml b")
kernel.saveBrain("G:\\Python27\\Lib\\site-packages\\aiml\\standard\\bot_brain.brn")

# kernel now ready for use
while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("G:\\Python27\\Lib\\site-packages\\aiml\\standard\\bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response
