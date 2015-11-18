import rospy
from std_msgs.msg import Int64
from Tkinter import *
import RPi.GPIO as GPIO
import time

main = Tk()

def talker(data):
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    hello_str = data
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()

def kp(event):
	if event.keysym == 'Right' :
		talker(13)
	elif event.keysym =='Left' :
		talker(11)
	else :
		talker(0)
def kr(event) :
	talker(0)

main.bind_all('<KeyPress>', kp)
main.bind_all('<KeyRelease>', kr)

main.mainloop()

GPIO.cleanup()


