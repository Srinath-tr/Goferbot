import speech
import speech_recognition as sr
import os

r = sr.Recognizer()
m = sr.Microphone()

def takeNote():
    sv = 0
    fnote = ""
    speech.say('ya sure, tell me')

    while True:
        print '>>input: '
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            # we need some sds pecial handling here to correctly print unicode characters to standard output
            if str is bytes:
                notes = format(value).encode("utf-8")
                notes = str.lower(notes)
                #note=notes
                print(notes)
                if 'save' in notes:
                    sv = 1
                    savePos = notes.find('save')
                    fnote = fnote + notes[:savePos]
                    print notes
                    speech.say('tell me a name for this note')
                    while True:
                        print '>>input: '
                        with m as source: audio = r.listen(source)
                        print("Got it! Now to recognize it...")
                        try:
                            # recognize speech using Google Speech Recognition
                            value = r.recognize_google(audio)
                            # we need some special handling here to correctly print unicode characters to standard output
                            if str is bytes:
                                noteName = format(value).encode("utf-8")
                                noteName = str.lower(noteName)
                                print noteName
                                break
                        except:
                            print 'no input'
                            continue
                                                            
                elif notes == 'save':
                    sv = 1
                    speech.say('tell me a name for this note')
                    while True:
                        print '>>input: '
                        with m as source: audio = r.listen(source)
                        print("Got it! Now to recognize it...")
                        try:
                            # recognize speech using Google Speech Recognition
                            value = r.recognize_google(audio)
                            # we need some special handling here to correctly print unicode characters to standard output
                            if str is bytes:
                                noteName = format(value).encode("utf-8")
                                noteName = str.lower(noteName)
                                print noteName
                                break
    
                        except:
                            print 'no input'
                            continue
                else:
                    fnote = fnote + notes
            if sv == 1:
                break
            else:
                continue
        except:
            print 'no input'
            continue
    _noteName = "notes\\" + noteName + '.txt'
    print 'saving note'
    file_note = open(_noteName, "w+")
    file_note.write(fnote)
    file_note.close()
    speech.say(noteName + ' is saved')


def speakNote(result):
    note_list = os.listdir("notes")
    for nl in note_list:
        if nl in result:
            _nl = nl[:len(nl)-4]
            print _nl
            filename = 'notes\\' + _nl + '.txt'
            print filename
            file_note = open(filename,"r")
            data = file_note.read()
            print data
            speech.say(data)
            break
    else:
        speech.say('what is the name of the note')
        while True:
            print '>>input: '
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:
                    noteName = format(value).encode("utf-8")
                    noteName = str.lower(noteName)
                    print noteName
                    break
            except:
                print 'no input'
                continue

        for nl in note_list:
            _nl = nl[:len(nl)-4]
            print _nl
            if _nl in noteName:
                filename = 'notes\\' + _nl + '.txt'
                print filename
                file_note = open(filename,"r")
                data = file_note.read()
                print data
                speech.say(data)
                break
