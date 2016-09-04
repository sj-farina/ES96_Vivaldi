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

FRONT = 1
BACK = 2
LEFT = 3
RIGHT = 4
STOP = 0


serialPort = Serial('/dev/ttyAMA0', 9600, timeout = 2)

motor1_cur = M1S
motor2_cur = M2S

def kp(event):
  #going to FRONT
	if event == 'w':
    if (cur_state == STOP)
      # 64 is starting, 127 is ending
      # 192 is starting , 255 is ending
      for x in (64, 128)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == BACK)
      # 1 is starting, 127 is ending
      # 128 is starting , 255 is ending
        for x in (1, 128)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == RIGHT)
      # 1 is starting, 127 is ending
      # 255 is starting , 255 is ending
      for x in (1, 128)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    elif (cur_state == LEFT)
      # 127 is starting, 127 is ending
      # 128 is starting , 255 is ending
      for x in (128, 256)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    serialPort.write(chr(M1F))
    serialPort.write(chr(M1F))
    cur_state = FRONT

  #going to BACK
	elif event == 's'
    if (cur_state == STOP)
      # 64 is starting, 1 is ending
      # 192 is starting , 128 is ending
      for x in (64, 0, -1)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == FRONT)
      # 127 is starting, 1 is ending
      # 255 is starting , 128 is ending
        for x in (127, 0, -1)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == RIGHT)
      # 1 is starting, 1 is ending
      # 255 is starting , 128 is ending
      for x in (255, 127, -1)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    elif (cur_state == LEFT)
      # 127 is starting, 1 is ending
      # 128 is starting , 128 is ending
      for x in (127, 0, -1)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    serialPort.write(chr(M1B))
    serialPort.write(chr(M1B))
    cur_state = BACK

  # going to RIGHT
  elif event == 'd':
    if (cur_state == STOP)
      # 64 is starting, 1 is ending
      # 192 is starting , 255 is ending
      for x in (64, 0, -1)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == FRONT)
      # 127 is starting, 1 is ending
      # 255 is starting , 255 is ending
        for x in (127, 0, -1)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == BACK)
      # 1 is starting, 1 is ending
      # 128 is starting , 255 is ending
      for x in (255, 127, -1)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    elif (cur_state == LEFT)
      # 127 is starting, 1 is ending
      # 128 is starting , 255 is ending
      for x in (127, 0, -1)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
	  serialPort.write(chr(M1B))
	  serialPort.write(chr(M2F))
    motor1_cur = M1B
    motor2_cur = M2F

  # going to LEFT
	elif direction == 'a':
    if (cur_state == STOP)
      # 64 is starting, 127 is ending
      # 192 is starting , 128 is ending
      for x in (64, 128)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == FRONT)
      # 127 is starting, 127 is ending
      # 255 is starting , 128 is ending
        for x in (255, 127, -1)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    elif (cur_state == BACK)
      # 1 is starting, 127 is ending
      # 128 is starting , 128 is ending
      for x in (1, 128)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    elif (cur_state == RIGHT)
      # 1 is starting, 127 is ending
      # 255 is starting , 128 is ending
      for x in (1, 128)
      	serialPort.write(chr(x))
      	serialPort.write(chr(x+127))
        print x
        print x + 127
        time.sleep(.01)
  	serialPort.write(chr(M1F))
	  serialPort.write(chr(M2B))
    motor1_cur = M1F
    motor2_cur = M2B

  # going to STOP
  else
    if (cur_state == RIGHT)
      # 1 is starting, 64 is ending
      # 255 is starting , 192 is ending
      for x in (1, 65)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == LEFT)
      # 127 is starting, 64 is ending
      # 128 is starting , 192 is ending
      for x in (127, 0, -1)
      	serialPort.write(chr(x))
        print x
        time.sleep(.01)
    elif (cur_state == FRONT)
      # 127 is starting, 64 is ending
      # 255 is starting , 192 is ending
        for x in (127, 63, -1)
      	serialPort.write(chr(x))
    		serialPort.write(chr(x+127))
        print x
        print x + 128
        time.sleep(.01)
    elif (cur_state == BACK)
      # 1 is starting, 64 is ending
      # 128 is starting , 192 is ending
      for x in (1, 65, -1)
      	serialPort.write(chr(x))
        serialPort.write(chr(x+127))
        print x
        print x + 127
        time.sleep(.01)
    serialPort.write(chr(M1S))
	  serialPort.write(chr(M2S))
    motor1_cur = M1S
    motor2_cur = M2S



while(1):
  datain = raw_data()
  kp(datain)



main.mainloop()

serialPort.close()

