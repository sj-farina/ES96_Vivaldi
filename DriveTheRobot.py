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

#setup
'''next_stateR = 0
next_stateL = 0
cur_stateR = 0
cur_stateL = 0
direction = 0'''

serialPort = Serial('/dev/ttyAMA0', 9600, timeout = 2)


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
	update()

def update():
	global cur_stateR
	global cur_stateL
	if (cur_stateR != next_stateR):
		#first set to 64
		cur_stateR = M1S
		cur_stateL = M2S
		refresh()
		time.sleep(1)
	  # then itterate to the desired stat
		if cur_stateR == M1F:
			for x in range (M1S, M1F):
				cur_stateR = x
				refresh()
		elif cur_stateR == M1B:
			for x in range (M1S, M1B, -1):
				cur_stateR = x
				refresh()
		  # then itterate to the desired state
		elif cur_stateL == M2F:
			for x in range (M2S, M2F):
				cur_stateL = x
				refresh()
		elif cur_stateR == M2B:
			for x in range (M2S, M2B, -1):
				cur_stateL = x
				refresh()
	refresh()

def refresh():
	serialPort.write(chr(cur_stateR))
	serialPort.write(chr(cur_stateL))
	print cur_stateR
	print cur_stateL


main.bind_all('<KeyPress>', kp)

main.mainloop()

serialPort.close()

