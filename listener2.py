import pigpio
import rospy
from std_msgs.msg import Int64
from Tkinter import *
#import RPi.GPIO as GPIO
import time


pi1 = pigpio.pi()


def callback(data):
	# GPIO expects an int, which is notthe same as Int64,
	# still need to figure out how to convert betweent he two >_<
	# This is a super messy workaround...
	stuff = str(data)
	tag, value = str.split(stuff)
	pin = int(value)
	if pin == 0:
		print ('off')
		off()
	else:
		print(pin)
		on(pin)

def off():
	pi1.write(17,0)
	pi1.write(18,0)
	#eventually make this an aray and loop thought pin
	#GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(11, GPIO.OUT)
	#GPIO.setup(13, GPIO.OUT)
	#GPIO.output(13,GPIO.LOW)
	#GPIO.output(11,GPIO.LOW)

def on(pin):
	pi1.write(pin, 1)
	#GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(pin, GPIO.OUT)
	#GPIO.output(pin,GPIO.HIGH)
	return



def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", Int64, callback)

    rospy.spin()



if __name__ == '__main__':
    listener()
