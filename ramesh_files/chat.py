import aiml
k = aiml.Kernel()
k.learn("audio2.aiml")

while True:
    rec = raw_input('>')
    reply = k.respond(rec)
    print reply
