#Kills roboclaw when s3 is connected to 
import pigpio
import time
pi1 = pigpio.pi()
pi1.write(2,0)
time.sleep(5)
pi1.write(2,1)

