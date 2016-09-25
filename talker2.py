# talker2.py
# Janey Farina, Alex Raun
# To be run with listener2.py, start roscore first
# GPOI 17 and 18 should be connected to LEDs


#This is the initial "Talking" or mesenger program 
#we used it to test connectivity and the ability to transmit keypresses 
#quickly and reliably over the network


import rospy
from std_msgs.msg import Int64
from Tkinter import *
import time

#start tkinter module
main = Tk()

#called by kp, initilized messenger node on roscore, sends key press data
def talker(data):
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rospy.loginfo(data)
    pub.publish(data)
    rate.sleep()

# called by main on key press event, sends key info to talker
def kp(event):
	if event.keysym == 'Right' :
		talker(18)
	elif event.keysym =='Left' :
		talker(17)
	else :
		talker(0)

#on keypress, call kp
main.bind_all('<KeyPress>', kp)

main.mainloop()

