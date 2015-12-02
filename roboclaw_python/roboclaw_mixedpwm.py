import time
import roboclaw
from serial import Serial

#Windows comport name
#roboclaw.Open("COM3",115200)
#Linux comport name
roboclaw.Open("/dev/ttyAMA0",9600)
#serialPort = Serial("/dev/ttyAMA0", 9600, timeout=2)

address = int(0x80)

roboclaw.ForwardMixed(address, 0)
roboclaw.TurnRightMixed(address, 0)

for x in range (0,127):
	roboclaw.ForwardM1(address, x)
	roboclaw.ForwardM2(address, x)
	time.sleep(.01)
	print x
'''while(1):
	roboclaw.ForwardM1(address, 64)
	time.sleep(.5)
        print 'foo'
	roboclaw.BackwardM1(address, 64)
	time.sleep(.5)
	print 'foo2'
	roboclaw.TurnRightMixed(address, 96)
	time.sleep(.5)
	roboclaw.TurnLeftMixed(address, 96)
	time.sleep(.5)
	roboclaw.ForwardMixed(address, 0)
	roboclaw.TurnRightMixed(address, 32)
	time.sleep(.5)
	roboclaw.TurnLeftMixed(address, 32)
	time.sleep(.5)
	roboclaw.TurnRightMixed(address, 0)
	time.sleep(.5)
'''
