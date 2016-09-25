# listener2.py
# Janey Farina, Alex Raun
# To be run with talker2.py, start roscore first
# GPOI 17 and 18 should be connected to LEDs


#This is the initial "Listening" or subscriber program 
#we used it to test connectivity and the ability to transmit keypresses 
#quickly and reliably over the network


#pigpio allows non-root acess to GPIO pins
import pigpio
import rospy
from std_msgs.msg import Int64
from Tkinter import *
import time

# initilize pigpio
pi1 = pigpio.pi()

# processes the info comming in from talker2.py and calls off or on
def callback(data):
	# GPIO expects an int, which is notthe same as Int64,
	# This is a super messy workaround converstion
	data64 = str(data)
	tag, value = str.split(data64)
	pin = int(value)
	if pin == 0:
		print ('off')
		off()
	else:
		print(pin)
		on(pin)

# turn all LEDs off
def off():
	pi1.write(17,0)
	pi1.write(18,0)

# turn specified LED on
def on(pin):
	print pin
	pi1.write(pin, 1)
	return


# subscriber that is listening for info from talker2.py
def listener():
    rospy.init_node('listener', anonymous=True)
	# when data is received, call callback
    rospy.Subscriber("chatter", Int64, callback)
    rospy.spin()



if __name__ == '__main__':
    listener()
