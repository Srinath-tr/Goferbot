#!/usr/bin/env python


from Arduino import Arduino
import time

board = Arduino('9600') #plugged in via USB, serial com at rate 9600
#board.pinMode(8, "OUTPUT")
#board.pinMode(9, "OUTPUT")

'''while True:
    board.digitalWrite(13, "LOW")
    time.sleep(1)
    board.digitalWrite(13, "HIGH")
    time.sleep(1)'''

'''##### Motor Shield (L298N) #####*/
* Arduino Pin --> L298N
* 5 --> ENA
* 6 --> ENB
* 2 --> IN1
* 3 --> IN2
* 4 --> IN3
* 7 --> IN4'''

ENA = 5
ENB = 6 
'''
* IN1: HIGH; IN2: LOW --> Direction 1 
* IN1: LOW; IN2: HIGH --> Direction 2
* IN3: HIGH; IN4: LOW --> Direction 1
* IN3: LOW; IN4: HIGH --> Direction2
'''
IN1 = 2 
IN2 = 3
IN3 = 4
IN4 = 7
 
#void setup()
#{
board.pinMode(ENA, 'OUTPUT');
board.pinMode(ENB, 'OUTPUT');
board.pinMode(IN1, 'OUTPUT');
board.pinMode(IN2, 'OUTPUT');
board.pinMode(IN3, 'OUTPUT');
board.pinMode(IN4, 'OUTPUT');
# Enable Motor A, Motor B: Constant Speed
board.digitalWrite(ENA, 'HIGH');
board.digitalWrite(ENB, 'HIGH');
# Serial communication
#board.Serial.begin(9600);
#}
 
def Motor_test():
    print("Motor A & B: Direction 1")
    MotorAB_Direction1(1)
    print("Motor A & B: Brake")
    MotorAB_Brake(1)
    print("Motor A & B: Direction 2")
    MotorAB_Direction2(1)
    print("Motor A & B: Brake")
    MotorAB_Brake(1)
    print("Motor A & B: Direction 2")
    MotorA_Direction1(1)
    print("Motor A : Direction 1")
    MotorA_Direction2(1)
    print("Motor A : Direction 2")
    MotorB_Direction1(1)
    print("Motor B : Direction 1")
    MotorB_Direction2(1)
    print("Motor B : Direction 2")
    MotorAB_Brake(1)
    print("Motor A & B: Brake")
 
def MotorAB_Direction1(seconds):
    board.digitalWrite(IN1, 'HIGH')
    board.digitalWrite(IN2, 'LOW')
    board.digitalWrite(IN3, 'HIGH')
    board.digitalWrite(IN4, 'LOW')
    if (seconds > 0):
        time.sleep(seconds)

 
def MotorAB_Direction2(seconds):
    board.digitalWrite(IN1, 'LOW')
    board.digitalWrite(IN2, 'HIGH')
    board.digitalWrite(IN3, 'LOW')
    board.digitalWrite(IN4, 'HIGH')
    if(seconds > 0):
        time.sleep(seconds)

def MotorA_Direction1(seconds):
    board.digitalWrite(IN1, 'HIGH')
    board.digitalWrite(IN2, 'LOW')
    board.digitalWrite(IN3, 'HIGH')
    board.digitalWrite(IN4, 'HIGH')
    if (seconds > 0):
        time.sleep(seconds)

 
def MotorA_Direction2(seconds):
    board.digitalWrite(IN1, 'LOW')
    board.digitalWrite(IN2, 'HIGH')
    board.digitalWrite(IN3, 'HIGH')
    board.digitalWrite(IN4, 'HIGH')
    if(seconds > 0):
        time.sleep(seconds)

def MotorB_Direction1(seconds):
    board.digitalWrite(IN1, 'HIGH')
    board.digitalWrite(IN2, 'HIGH')
    board.digitalWrite(IN3, 'HIGH')
    board.digitalWrite(IN4, 'LOW')
    if (seconds > 0):
        time.sleep(seconds)

 
def MotorB_Direction2(seconds):
    board.digitalWrite(IN1, 'HIGH')
    board.digitalWrite(IN2, 'HIGH')
    board.digitalWrite(IN3, 'LOW')
    board.digitalWrite(IN4, 'HIGH')
    if(seconds > 0):
        time.sleep(seconds)

def MotorAB_Brake(seconds):
    board.digitalWrite(IN1, 'HIGH')
    board.digitalWrite(IN2, 'HIGH')
    board.digitalWrite(IN3, 'HIGH')
    board.digitalWrite(IN4, 'HIGH')
    if(seconds > 0):
        time.sleep(seconds)

#Motor_test()
#MotorAB_Direction1(1)
#MotorAB_Brake(1)
