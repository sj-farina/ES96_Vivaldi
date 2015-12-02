import time
import roboclaw

#Windows comport name
#roboclaw.Open("COM3",115200)
#Linux comport name
roboclaw.Open("/dev/tty0",115200)

address = 0x80

roboclaw.ForwardMixed(address, 0)
roboclaw.TurnRightMixed(address, 0)

while(1):
	roboclaw.ForwardM1(address, 64)
	time.sleep(2)
        print 'foo'
	roboclaw.BackwardM1(address, 64)
	time.sleep(2)
	print 'foo2'
	roboclaw.TurnRightMixed(address, 64)
	time.sleep(2)
	roboclaw.TurnLeftMixed(address, 64)
	time.sleep(2)
	roboclaw.ForwardMixed(address, 0)
	roboclaw.TurnRightMixed(address, 64)
	time.sleep(2)
	roboclaw.TurnLeftMixed(address, 64)
	time.sleep(2)
	roboclaw.TurnRightMixed(address, 0)
	time.sleep(2)
