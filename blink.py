################################
# Controls: left and right arrow keys
#LEDs on pin 11 and 13 will light while 
#corresponding arrow key is held down
################################


import RPi.GPIO as GPIO
import time
from Tkinter import *

main = Tk()

def kp(event):
	if event.keysym == 'Right' :
		on(13)
	elif event.keysym =='Left' :
		on(11)
	else :
		return

def kr(event):
	off()

def off():
	#eventually make this an aray and loop thought pin
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(11,GPIO.LOW)
	
def on(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)
	return


main.bind_all('<KeyPress>', kp)
main.bind_all('<KeyRelease>', kr)

main.mainloop()

GPIO.cleanup()
