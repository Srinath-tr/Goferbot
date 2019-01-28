from Tkinter import*
import time
import datetime
from multiprocessing import Process
import sys
from urllib2 import urlopen
#count=0
ref = 0
root=Tk()
now=datetime.datetime.now()
date = ''
time1 = ''
title="KLN College of Engineering"
title_box=Label(root,text=title, font=("Times",50),fg="black",bg="light blue")
title_box.pack(fill=BOTH, expand=1)
clock = Label(root,justify=RIGHT, font=('times', 30, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
date_now = Label(root, font=('times', 30, 'bold'), bg='white')
date_now.pack(fill=BOTH, expand=1)
footer="Developed by MICRO-ELECTRONICS CLUB of ECE, KLNCE"
footer_box=Label(root, text=footer, font=("Times",40),fg="black",bg="light blue")
footer_box.pack(side=BOTTOM, fill=BOTH, expand=1)

 #frame=Frame(root,width=100,height=100,relief='solid')
# frame.place(x=10,y=10)
 #text=Label(root,text=msg.upper(), font=("Times new roman",70),fg="blue",bg="white", height=120, width=200, wraplength=1500)
#text.pack()

def tick():
    global time1
    time2 = time.strftime('                                                                                                                                                 %H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
def date():
    global date_now
    date=now.strftime("                                                                                                                                              %Y-%m-%d")
    date_now.config(text=date)
    
def Draw():
  global text
  global ref
  #global msg1
  msg_url = "http://klnenotice.16mb.com/messageStatus.php?count=" + str(ref)
  msg = urlopen(msg_url).read()
  frame=Frame(root,width=100,height=100,relief='solid')
  frame.place(x=10,y=10)
  text=Label(root,text=msg.upper(), font=("Times new roman",70),fg="blue",bg="white", height=120, width=200, wraplength=1500)
  text.pack()

def Refresher():
 global text
 global ref
 global msg_url
 global msg1
 msg_url = "http://klnenotice.16mb.com/messageStatus.php?count=" + str(ref)
 msg = urlopen(msg_url).read()
 #frame=Frame(root,width=100,height=100,relief='solid')
#frame.place(x=10,y=10)
 #text=Label(root,text=msg.upper(), font=("Times new roman",70),fg="blue",bg="white", height=120, width=200, wraplength=1500)
 #text.pack()
 
 #global var
 #ref = ref + 1
 #if ref > 2:
 #	ref = 0
 print ref
 msg_url = "http://klnenotice.16mb.com/messageStatus.php?count=" + str(ref)
 msg = urlopen(msg_url).read()
 msg1=msg
 count=0
 #text.config(text=msg.upper())
 #root.after(2000, Refresher)
 while((msg1==msg) & (count<5)):        
     print msg
     #text=Label(root,text=msg.upper(), font=("Times new roman",70),fg="blue",bg="white", height=120, width=200, wraplength=1500)
     #text.pack()
     text.config(text=msg1.upper())
    
     #root.after(2000, Refresher)
     #msg1=msg
     msg=urlopen(msg_url).read()
     time.sleep(1)
     count+=1
     root.update()
 while((msg1==msg) & (count>=5)):
     default_msg="welcome to klnce "
     print default_msg
    # text=Label(root,text=msg.upper(), font=("Times new roman",70),fg="blue",bg="white", height=120, width=200, wraplength=1500)
    # text.pack()
     text.config(text=default_msg.upper())
     #root.after(2000, Refresher)
     msg1=msg
     msg=urlopen(msg_url).read()
     time.sleep(1)
     root.update()
 msg_new=urlopen(msg_url).read()
 #msg_new=msg
 #msg_new=match(msg,msg1)
 #msg_new=match1(msg,msg1)
 #p1 = Process(target = func_sleep)
 #p1.start()
 #if(func_sleep().var==0):
 #    text.config(text=msg.upper())
 #else:
 #    text.config(text="WELCOME TO KLNCE")
 #text.config(text=msg.upper())
 text.config(text=msg_new.upper())
 root.after(2000, Refresher)
 

#def match(msg_now,msg2):
 #   global text
   # global msg1
   # frame=tk.Frame(root,width=100,height=100,relief='solid')
   # frame.place(x=10,y=10)
   # text1=tk.Label(root,text=msg2.upper(), font=("Times new roman",70),fg="blue",bg="white", height=120, width=200, wraplength=1500)
   # print text1
   # text1.pack()
   # text1.config(text=msg_now.upper())
  #  count=0
   # if((msg2==msg_now) & (count<10)):
   #     print msg_now
   #     text.config(text=msg_now.upper())
   #     msg2=msg_now
   #     msg_now=urlopen(msg_url).read()
   #     time.sleep(1)
   #     count+=1
   #     #return msg_now
   #     text.after(100,match(msg_now,msg2)
   # #else:
   #  #   return msg_now
                   
#def match1(msg_now,msg2):
   #                global text
   #                global count
   #                if((msg2==msg_now) & (count>=10)):
   #                default_msg="welcome to klnce "
   #                print default_msg
   #                text.config(text=default_msg.upper())
   #                msg2=msg_now
   #                msg_now=urlopen(msg_url).read()
   #                time.sleep(1)
   #                #return msg_now           
   #                text.after(100,match(msg_now,msg2)
   # #else:
   #  #   return msg_now
      
tick()
date()
root.title("Message Banner")
root.attributes("-fullscreen",True)
#title()
Draw()
Refresher()
#root.after(2000,Refresher)
root.mainloop()
