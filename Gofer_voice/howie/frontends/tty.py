import random
import sys
import os
import time
import pyttsx
import re
import random
import speech
import speech_recognition as sr
import frontend
import GoogleText
import requests
import subprocess
from remainder import addActivity
#import storeImage
import notes
import captureImage
# This string needs to be defined for each front end.  It should
# contain the name of the front-end class defined in this module.
frontEndClass = "FrontEndTTY"

# List the default values for the INI file.  This should be a dictionary
# with keys of the form "<fe>.<entry>", where <fe> is the name of the
# frontend (e.g. "aim", "msn"), and entry is the name of the configuration
# variable (e.g. "username", "password").  All values should be strings.
#
# Each frontend must define an "active" entry, whose possible values
# are "yes" and "no", which indicates whether that frontend should
# be activated.

configDefaults = {
    "tty.active":       "yes"
    }

r = sr.Recognizer()
m = sr.Microphone()

#os.path.dirname(os.path.realpath(__file__))

class FrontEndTTY(frontend.IFrontEnd):  
    """
    A butt-simple class demonstrating the bare minimum needed to
    implement a new front-end for Howie.
    """
    def go(self):
        post_cmd = "http://goferiot.16mb.com/default.php"
        tag = 'price of','cost of','rate of','prize of'
        iot = 'lights on','lights off','lights of','light on','light of','switch on the light','switch off the light','switch off light','switch on the fan','switch on fan','switch off the fan','switch of the light','switch of the fan'
        gofer = 'gofer','goplher','gopher','gophers','go for','sofa','go far','gofa','zafar','buffer','gufa','lofer','lofar','loafer','gopal','gophar','goper','gopar','go fur'
        hello = 'hello','hallo','helo','halo','hi','hai','high'
        capture = 'capture','take','click'
        image = 'photo','picture','image','snap'
        add = 'add','include','save','store','scan','spur','see'
        face = 'face','fase','fac','phase'
        get_name = 'my name is ','myname is','this is ','i am ','im ',"i'm","am ",'myself ','my self '
        speak = 'tell','read','speak','say'
        remainder = 'remind','remainder','remain','alert'
        call = 'come','move','turn','go','stop','step'
        
        self._sessionID = "localhost@TTY"
        import howie.core
        howie.core.kernel.setPredicate("secure", "yes", self._sessionID)
        
        subprocess.call(['python',r'G:\Python27\Gofer_voice\face_start.py'],cwd=r'G:\Python27\Gofer_voice')
        subprocess.Popen(['python','remainder_checktime.py'])
        
        while True:
            #input = raw_input(">>> ")
            print ">>input: "
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:
                    result = format(value).encode("utf-8")
                    result = str.lower(result)
                    print(result)
            except:
                print 'no input'
                #speech.say('check your internet connection')
                continue
            fl=0
            for g in gofer:
                if g in result:
                    #print 'inside gofer'
                    #fl = 0
                    for h in hello:
                        if h in result:
                            fl = 1
                            print 'starting face recognition'
                            subprocess.call(['python',r'G:\Python27\Gofer_voice\facerec_model.py'],cwd=r'G:\Python27\Gofer_voice')
                            #facerec_model.startapp(mod,camid,filename)  
                            break
                #break
                    if fl==1:
                        break
                        
                    else:
                        for c in capture:
                            if c in result:
                                for i in image:
                                    if i in result:
                                        fl=1
                                        speech.say('smile please')
                                        captureImage.capture()
                                        print 'image taken.!'
                                        speech.say('image taken')
                                        break
                        else:
                            for a in add:
                                if a in result:
                                    for f in face:
                                        if f in result:
                                            fl=1
                                            speech.say("tell me your name")
                                            while True:
                                                with m as source: audio = r.listen(source)
                                                print("Got it! Now to recognize it...")
                                                try:
                                                    # recognize speech using Google Speech Recognition
                                                    value = r.recognize_google(audio)
                                                    # we need some special handling here to correctly print unicode characters to standard output
                                                    if str is bytes:
                                                        name = format(value).encode("utf-8")
                                                        name = str.lower(name)
                                                        print(name)
                                                    for gn in get_name:
                                                        if gn in name:
                                                            name = name[len(gn):]
                                                            break
                                                    print 'folder name: ' + name
                                                    fpath = 'G:\\Python27\\Faces\\' + str(name)
                                                    print 'path: ' + fpath
                                                    if not os.path.exists(fpath):
                                                        os.makedirs(fpath)
                                                        #subprocess.Popen(['python',"img_store_worked.py"])
                                                        fpath = fpath + '\\' + str(name)
                                                        print 'storepath: ' + fpath
                                                        #storeImage.store(fpath)
                                                        subprocess.call(['python','storeImage.py',name])
                                                        subprocess.Popen(['python','facerec_add.py','-t',"G:\Python27\Faces",'my_model.pkl'])
                                                        print 'face added to database'
                                                        speech.say('your face is added to my database')
                                                        break
                                                    else:
                                                        print 'folder already exists in this path'
                                                        speech.say('folder already exists in this path. Tell me your initial or nick name')
                                                        continue
                                                except:
                                                    print 'no input'
                                                    continue                                            
                                
                                        if fl==1:
                                            fl=0
                                            break
                                                                        
                            else:
                                if 'date' in result:
                                    fl=1
                                    print 'inside date'
                                    gdate = time.strftime("%d/%m/%Y")
                                    print "today's date is " + gdate
                                    speech.say("today's date is " + gdate)
                                    #break
                                    continue
                                elif 'time' in result:
                                    fl=1
                                    print 'inside tme'
                                    gtime = time.strftime("%I:%M")
                                    print 'time is  ' + gtime
                                    speech.say('the time now is ' + gtime)                                          
                                    #break
                                    continue
                                elif 'note' in result:
                                    fl=1
                                    sn = 0
                                    print 'note in result'
                                    for sp in speak :
                                        if sp in result:
                                            sn = 1
                                            print 'speaking note'
                                            notes.speakNote(result)
                                            break
                                    if sn == 1:
                                        sn = 0
                                        continue
                                    else:
                                        notes.takeNote()
                                        #break
                                        continue
                                else:
                                    for ca in call:
                                        if ca in result:
                                            fl=1
                                            subprocess.Popen(['python',r'G:\Python27\controlRover.py',result])

                                    else:
                                        for rem in remainder:
                                            if rem in result:
                                                fl=1
                                                addActivity(result)
                                                break
                                    
            if fl==1:
                fl=0
                continue
            
            else:
                #print 'tag sommar'
                for t in tag:
                    if t in result:
                        print 'ok, let me search in the net'
                        speech.say('ok, let me search in the net')
                        GoogleText.price_search(result)
                        break
                else:
                    #print 'iot sommar'
                    io = 0
                    for i in iot:
                        if i in result:
                            io = 1
                            form_data={
                                'text_box':result,
                                'search-submit':'submit',
                                }
                            try:
                                requests.post(post_cmd, data=form_data)
                                #print 'just a second'
                                speech.say('just a second')
                                break
                            except:
                                print "can't connect to the internet"
                                break
                    if io == 0:
                    #else:
                        print 'executing'
                        response = self.submit(result, self._sessionID)
                        if response==" ":
                            response = 'sorry, can you rephrase your input'
                        self.display(response, self._sessionID)
                        #print 'next'
        
    def display(self, output, user):
        try:
            if str is bytes:
                #print "printing output"
                print output
                speech.say(output)
        except:
            print 'speech exception'
