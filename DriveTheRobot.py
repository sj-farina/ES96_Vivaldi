import rospy
from std_msgs.msg import Int64
from Tkinter import *
import time


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
next_stateR = 0
next_stateL = 0
cur_stateR = 0
cur_stateL = 0


main = Tk()


def kp(event):
	if event.keysym == 'Up' :
    direction = F
  elif event.keysym =='Down' :
    direction = B
  elif event.keysym =='Left' :
    direction = L
  elif event.keysym =='Right' :
    direction = R
	else :
    direction = S


case (direction)
  F : begin
    next_stateR = M1F
    next_stateL = M2F
  end
  B : begin
    next_stateR = M1B
    next_stateL = M2B
  end
  R : begin
    next_stateR = M1B
    next_stateL = M2F
  end
  L : begin
    next_stateR = M1F
    next_stateL = M2B
  end
  S : begin
    next_stateR = M1S
    next_stateL = M2S
  end
  default : begin
    next_stateR = M1S
    next_stateL = M2S
  end
endcase

if (cur_stateR != next_stateR)
  #first set to 64
  cur_stateR = M1S
  cur_stateL = M2S
  time.sleep(1)
  # then itterate to the desired state
  case (next_stateR)
    M1F : begin
      for x in range (M1S, M1F)
        cur_stateR = x
    end
    M1B : begin
      for x in range (M1S, M1B, -1)
        cur_stateR = x
    end
  endcase
  # then itterate to the desired state
  case (next_stateL)
    M2F : begin
      for x in range (M2S, M2F)
        cur_stateL = x
    end
    M2B : begin
      for x in range (M2S, M2B, -1)
        cur_stateL = x
    end
  endcase


serialPort.write(chr(cur_stateR))
serialPort.write(chr(cur_stateL))
print cur_stateR
print cur_stateL


main.bind_all('<KeyPress>', kp)

main.mainloop()

serialPort.close()

