import rospy
from std_msgs.msg import Int64
from Tkinter import *
import time

main = Tk()

S = 0
F = 1
B = 2
L = 3
R = 4


def talker(data):
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    pub.publish(data)
    rate.sleep()

def kp(event):
	if event.keysym == 'Up' :
		talker(F)
	elif event.keysym =='Down' :
		talker(B)
	elif event.keysym =='Left' :
		talker(L)
	elif event.keysym =='Right' :
		talker(R)
	else :

		talker(S)
#def kr(event) :
#	talker(0)

main.bind_all('<KeyPress>', kp)
#main.bind_all('<KeyRelease>', kr)

main.mainloop()

