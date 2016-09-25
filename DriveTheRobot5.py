# DriveTheRobot5.py
# Janey Farina, Alex Raun
# To be run with DriveTheRobotGUI.py

#This program contorls the motors via the Roboclaw Driver

from Tkinter import *
import time
from serial import Serial
from std_msgs.msg import Int64
import rospy

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

# open the serial port and define initial values to be motors off
serialPort = Serial('/dev/ttyAMA0', 9600, timeout = 2)
cur_stateR = M1S
cur_stateL = M2S
next_stateR = M1S
next_state = M2S


def callback(data):
	# if the values have not been initialized, fix that
	try:
		cur_stateR
		cur_stateL

	except (ValueError, NameError):
		cur_stateR = 0
		cur_stateL = 0
		save_cur_state(0,0)
	# changing the Int64 to an int
	dataIn = str(data)
	tag, value = str.split(dataIn)
	input_int = int(value)
	direction_set(input_int)

# processes front back left right into motor directions
def direction_set(direction):
	if direction == F:
		next_stateR = M1F
		next_stateL = M2F
	elif direction == B:
		next_stateR = M1B
		next_stateL = M2B
	elif direction == R:
		next_stateR = M1B
		next_stateL = M2F
	elif direction == L:
		next_stateR = M1F
		next_stateL = M2B
	elif direction == S:
		next_stateR = M1S
		next_stateL = M2S
	else:
		next_stateR = M1S
		next_stateL = M2S
	update(next_stateR, next_stateL)

# compares the states of the motors with the next state and decided if to update
def update(next_stateR, next_stateL):
	cur_stateR, cur_stateL = get_cur_state()
	if (cur_stateR != next_stateR):
		#first set to 64 
		cur_stateR = M1S
		refresh(cur_stateL, cur_stateR)
		time.sleep(.01)
		cur_stateR = next_stateR


	print cur_stateL
	print next_stateL
	if (cur_stateL != next_stateL):
		#first set to 64
		cur_stateL = M2S
		refresh(cur_stateL, cur_stateR)
		time.sleep(.01)
		cur_stateL = next_stateL

	#print 'to save:'
	#print cur_stateR
	#print cur_stateL	
	save_cur_state(cur_stateL, cur_stateR)

# writes values to serial out
def refresh(cur_stateR, cur_stateL):
	serialPort.write(chr(cur_stateR))
	serialPort.write(chr(cur_stateL))
	print cur_stateR
	print cur_stateL

# saving the current state of the motors for comparison 
def save_cur_state(cur_stateR, cur_stateL):
	global cur_stateR_save
	global cur_stateL_save
	cur_stateR_save = cur_stateR
	cur_stateL_save	= cur_stateL
	#print cur_stateL_save
	#print cur_stateR_save

# returns current state for comparison
def get_cur_state():
	global cur_stateR_save
	global cur_stateL_save
	cur_stateR = cur_stateR_save
	cur_stateL = cur_stateL_save
	return(cur_stateL, cur_stateR)

#listener over roscore
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

#this should need to be in the talker code, not this. 
#main.bind_all('<KeyPress>', listener)


main.mainloop()

serialPort.close()

