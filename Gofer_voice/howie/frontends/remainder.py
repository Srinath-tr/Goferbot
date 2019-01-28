import sys
import time
import speech
#import speech_recognition as sr
import hear
import pandas as pd
import os

#r = sr.Recognizer()
#m = sr.Microphone()
remind = 'remind','remainder','remain','alert'
to = 'to','too','two','2','about'
units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

scales = ["hundred", "thousand", "million", "billion", "trillion"]

csvFileName = "G:\\Python27\\Gofer_voice\\remainders\\remainders.csv"
df = pd.read_csv(csvFileName)
#newl_flag = 0

def text2int(textnum, numwords={}):
    
    if not numwords:
      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    c=0
    for word in textnum.split():
        #print 'word: ' + word
        #print 'idx: ' + str(idx)
        if word not in numwords:
            #raise Exception("Illegal word: " + word)
            continue
        scale, increment = numwords[word]
        #print 'scale' + str(c) + str(scale)
        #print 'increment' + str(c) + str(increment)
        #print 'current_word: ' + str(current*scale)
        current = current * scale + increment
        #print 'current' + str(c) + str(current)
        c=c+1
        if scale > 100:
            result += current
            current = 0
    return result + current


'''def remainder():
    while True:
        alert = checkTime()
        speech.say(alert)
        removeActivity()'''

def removeActivity(index):
    csvFileName = "G:\\Python27\\Gofer_voice\\remainders\\remainders.csv"
    df = pd.read_csv(csvFileName)
    df.activity[index] = ''
    df.time[index] = ''
    #newl_flag = 1
    
def checkTime():
    while True:
        csvFileName = "G:\\Python27\\Gofer_voice\\remainders\\remainders.csv"
        df = pd.read_csv(csvFileName)
        remainder_time = df.time #you can also use df['column_name']
        gdate = time.strftime("%d/%m/%Y")
        gtime = time.strftime("%I:%M")
        print gdate + ',' + gtime
        print remainder_time
        print len(remainder_time)
        if gtime in remainder_time:
            print remainder_time.index(gtime)
            print 'yes'
        #print df.activity[3]
        i=0
        for rem in remainder_time:
            i=i+1
            if rem == gtime:
                print 'you got a remainder'
                print df.activity[i-1]
                speech.say('you got a remainder')
                speech.say(df.activity[i-1])
                removeActivity(i-1)
        print 'sleeping'
        time.sleep(30)
    

def addActivity(result):

    for  t in to:
        if t in result:
            tpos = result.find(t)
            factivity = result[tpos+len(t):]
            print factivity
            r_time = get_time(result)
            while r_time == -1:
                speech.say('set the time of the remainder')
                r_time = hear.hear()
                r_time = get_time(r_time)
                if r_time == -1:
                    speech.say('that is an invalid time format')
            break
        
    else:                             
        speech.say('ya sure, what sbould i remind you of')
        factivity = hear.hear()
        print factivity
        r_time = get_time(factivity)
        if r_time == -1:
            speech.say('set the time of the remainder')
            r_time = hear()
            r_time = get_time(r_time)

    rem_list = os.listdir("G:\\Python27\\Gofer_voice\\remainders")
    #count = len(rem_list) + 1
    remainderFile = "G:\\Python27\\Gofer_voice\\remainders\\remainders.csv"
    factivity = str(r_time) + ',' + str(factivity)
    print 'saving remainder'
    file_remainder = open(remainderFile, "a")
    file_remainder.write('\n' + factivity)
    file_remainder.close()
    speech.say(factivity + ' is saved')
    
            
#checkTime()

def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return 'T'
    except ValueError:
        return 'F'
    
def get_time(con):
    #con = 'remaind me at two forty five'
    words = con.split()
    f_hr = 0
    mm = 0
    re_time = ''
    print words        
    for w in words:
        if isTimeFormat(w) == 'T':
            re_time = str(w)
            break
        elif w.isdigit():
            if f_hr == 0 and 0 < int(w) <= 12:
                hr = int(w)
                if hr<10:
                    hr = "%02d" % hr
                print 'hr: ' + str(hr)
                f_hr = 1
            elif f_hr == 1:
                mm = mm + int(w)
        else:
            num = text2int(w)
            print num
            if f_hr == 0 and 0 < num <= 12:
                hr = num
                if hr<10:
                    hr = "%02d" % hr
                print 'hr: ' + str(hr)
                f_hr = 1
            elif f_hr == 1:
                mm = mm + num
            
    if f_hr == -1:
        print 'invalid time'
        return -1
    if mm <= 10:
        mm = "%02d" % mm
    if re_time == '':
        re_time = str(hr) + ':' + str(mm)
        
    print re_time
    return re_time

#addActivity('set a remainder to do the science assignment at nine twelve')
#checkTime()
#time = get_time('set the remainder at 10 10')
#print time

