import time
import sys
import PyRoverArduino

d_right = 'right','wright','write','rite','ryte'
d_left = 'left','lift','lef'
d_forward = 'front','forward','for ward','fore ward','here','to me','tome','frond'
d_back = 'back','backwards','bak','bag','back wards','backward','back ward'

#PyRoverArduino.Motor_test()

command = str(sys.argv[1:])
command = command.translate(None, "[']")
#command = 'come front'
print command
time.sleep(2)


for f in d_forward:
    if f in command:
        print 'inside front'
        PyRoverArduino.MotorAB_Direction1(1)
        PyRoverArduino.MotorAB_Brake(1)
        break
else:
    for b in d_back:
        if b in command:
            PyRoverArduino.MotorAB_Direction2(1)
            PyRoverArduino.MotorAB_Brake(1)
            break

    else:
        for l in d_left:
            if l in command:
                PyRoverArduino.MotorB_Direction1(1)
                PyRoverArduino.MotorAB_Brake(1)
                break

        else:
            for r in d_right:
                if r in command:
                    PyRoverArduino.MotorAB_Direction1(1)
                    PyRoverArduino.MotorAB_Brake(1)
                    break
