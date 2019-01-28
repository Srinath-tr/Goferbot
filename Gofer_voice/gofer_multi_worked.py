import subprocess

#subprocess.Popen(['python',"facerec_add.py",'-t',"G:\Python27\Faces",'my_model.pkl'])
#subprocess.Popen(['python',"facerec_model.py"])
#subprocess.Popen(['python', "G:/Python27/Gofer_voice/runme.py"]) 
#subprocess.Popen(['python', "process1.py"]) 
#subprocess.Popen(['python',"process2.py"])
name = r"gos"
subprocess.call(['python','storeImage.py',name])
