import rospy
from std_msgs.msg import Int64
from Tkinter import *
import time
from serial import Serial
from multiprocessing import Process


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


#serialPort = Serial('/dev/ttyAMA0', 9600, timeout = 2)
cur_stateR = M1S
cur_stateL = M2S
next_stateR = M1S
next_state = M2S

main = Tk()


def kp(event):
	if event.keysym == 'Up' :
		direction_set(F)
	elif event.keysym =='Down' :
		direction_set(B)
	elif event.keysym =='Left' :
		direction_set(L)
	elif event.keysym =='Right' :
		direction_set(R)
	else :
		save_cur_state(0, 0)
		direction_set(S)


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

def update(next_stateR, next_stateL):
	cur_stateR, cur_stateL = get_cur_state()
	if (cur_stateR != next_stateR):
		p1 = Process(target = motor1)
		p1.start()

	if (cur_stateL != next_stateL):
		p2 = Process(target = motor2)
		p2.start()

def motor1(cur_stateR):
	#first set to 64 
	print 'start motor1'
	cur_stateR = M1S
	refresh(cur_stateL, cur_stateR)
	time.sleep(1)
  	# then itterate to the desired stat
	if next_stateR == M1F:
		for x in range (M1S, M1F):
			cur_stateR = x
			time.sleep(.01)
			refresh(cur_stateL, cur_stateR)
	elif next_stateR == M1B:
		for x in range (M1S, M1B, -1):
			cur_stateR = x
			time.sleep(.01)
			refresh(cur_stateL, cur_stateR)
	save_cur_state(cur_stateL, cur_stateR)
	print 'end motor1'



def motor2(cur_stateL):
	#first set to 64
	print 'start motor2'
	cur_stateL = M2S
	refresh(cur_stateL, cur_stateR)
	time.sleep(1)
  	# then itterate to the desired stat
	if next_stateL == M2F:
		for x in range (M2S, M2F):
			cur_stateL = x
			time.sleep(.01)
			refresh(cur_stateL, cur_stateR)
	elif next_stateL == M2B:
		for x in range (M2S, M2B, -1):
			cur_stateL = x
			time.sleep(.01)
			refresh(cur_stateL, cur_stateR)
	save_cur_state(cur_stateL, cur_stateR)
	print 'end motor2'


p1 = threading.Thread(target=motor1, args=(cur_stateR))
p2 = threading.Thread(target=motor2, args=(cur_stateL))

def refresh(cur_stateR, cur_stateL):
	#serialPort.write(chr(cur_stateR))
	#serialPort.write(chr(cur_stateL))
	print cur_stateR
	print cur_stateL

def save_cur_state(cur_stateR, cur_stateL):
	global cur_stateR_save
	global cur_stateL_save
	cur_stateR_save = cur_stateR
	cur_stateL_save	= cur_stateL
	#print cur_stateL_save
	#print cur_stateR_save


def get_cur_state():
	global cur_stateR_save
	global cur_stateL_save
	cur_stateR = cur_stateR_save
	cur_stateL = cur_stateL_save
	return(cur_stateL, cur_stateR)


main.bind_all('<KeyPress>', kp)


main.mainloop()

serialPort.close()

