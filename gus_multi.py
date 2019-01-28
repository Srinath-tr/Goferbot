import os
import sys
import subprocess
#import pipe
#os.system('python wpy.py')
#print 'gos'
#os.system()
procs = []

proc = subprocess.Popen(['wpy.py'],shell=True)
procs.append(proc)
proc1 = subprocess.Popen(['gofer_iot.py'],shell=True)
procs.append(proc1)

proc.wait()
