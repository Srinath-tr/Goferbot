'''import storeImage
import time
import speech
import face_start
import subprocess
date = time.strftime("%d/%m/%Y")
speech.say(date)
print "today's date is " + date
time = time.strftime("%I:%M")
speech.say(time)
print 'time is  ' + time
#storeImage.store('G:\\Python27\\Faces\\gos\\gos')
#subprocess.call(['python','face_start.py'])
print 'ok'
noteName = 'notes\\akuchi' + '.txt'
print 'saving note'
file_note = open(noteName, "w+")
file_note.write('gos kono b')
file_note.close()'''

#import glob
import os
import notes
#print glob.glob('notes\\*.txt')
a=os.listdir("notes")
print a
notes.speakNote('adress')


