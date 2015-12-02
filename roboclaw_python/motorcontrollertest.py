import RPi.GPIO as GPIO
import time
import roboclaw
roboclaw.Open("/dev/tty0",115200)
address = 0x80
roboclaw.ForwardMixed(address,0)
event = raw_input("Give me a direction")
def kp(event):
	if event.keysym == "Right" :
		on(13)
	elif event.keysym == "Left" :
		on(11)
	else :
		return

def kr(event):
	off()

def off():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)

def on(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, GPIO.roboclaw.ForwardMixed(address, 64))
	time.sleep(2)
 
