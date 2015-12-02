from serial import Serial
import time

serialPort = Serial("/dev/ttyAMA0", 9600, timeout=2)
if (serialPort.isOpen() == False):
    serialPort.open()

for x in range(0,256,25):

	serialPort.flushInput()
	serialPort.flushOutput()

	#serialPort.write('%d' % (x))
	serialPort.write(chr(x))
	print '%d' % (x)
	time.sleep(1)
	'''serialPort.write('1')
	time.sleep(2)
	serialPort.write('64')
	time.sleep(2)
	serialPort.write('127')
	time.sleep(2)'''
    
serialPort.write(chr(0))
print 'for loop is done'


serialPort.close()
