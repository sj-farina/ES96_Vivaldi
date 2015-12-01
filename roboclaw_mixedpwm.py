import time
import roboclaw

#Windows comport name
#roboclaw.Open("COM3",115200)
#Linux comport name
roboclaw.Open("/dev/tty0",115200)

address = 0x80

roboclaw.ForwardMixed(address, 0)
roboclaw.TurnRightMixed(address, 0)
response = raw_input("Give me a number: ")
#while(1):
#	response = raw_input("Give me a number: ")
if response == '1':
	roboclaw.ForwardMixed(address, 64)
        print '1'
	time.sleep(2)
elif response == '2':
	roboclaw.BackwardMixed(address, 64)
        print '2'
	time.sleep(2)
elif response == '3':
	roboclaw.TurnRightMixed(address, 64)
        print '3'
	time.sleep(2)
else:
	print 'Only input 1, 2, or 3!!!'


	'''roboclaw.TurnLeftMixed(address, 64)
	time.sleep(2)
	roboclaw.ForwardMixed(address, 0)
	roboclaw.TurnRightMixed(address, 64)
	time.sleep(2)
	roboclaw.TurnLeftMixed(address, 64)
	time.sleep(2)
	roboclaw.TurnRightMixed(address, 0)
	time.sleep(2)'''
