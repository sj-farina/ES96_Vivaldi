import rospy
from std_msgs.msg import Int64
from Tkinter import *
import time
from serial import Serial

#Defines
M1B = 1
M1S = 64
M1F = 127
M2B = 128
M2S = 192
M2F = 255

S = 0
F = 1
B = 2
L = 3
R = 4


serialPort = Serial('/dev/ttyAMA0', 9600, timeout = 2)
cur_stateR = M1S
cur_stateL = M2S
next_stateR = M1S
next_state = M2S

def kp(event):
	print event
	if event == 'w' :
		serialPort.write(chr(127))
		serialPort.write(chr(255))
	elif event =='s' :
		serialPort.write(chr(1))
		serialPort.write(chr(128))
	elif event =='a' :
		serialPort.write(chr(128))
		serialPort.write(chr(127))
	elif event =='d' :
		serialPort.write(chr(1))
		serialPort.write(chr(255))
	else :
		serialPort.write(chr(64))
		serialPort.write(chr(192))

while(1):
	datain = raw_input()
	kp(datain)
	
