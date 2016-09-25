#python 3
#from tkinter import *
#from tkinter import ttk

#python 2
from Tkinter import *
import ttk

import rospy
from std_msgs.msg import Int64
import time
import subprocess
import paramiko

import threading


#defines

Stop = 0
Front = 1
Back = 2
Left = 3
Rright = 4

# keep track of widgets for event handlers
widget_track = {}




class Find_Joystick:
	def __init__(self, root):
		self.root = root

		## initialize pygame and joystick
		pygame.init()
		if(pygame.joystick.get_count() < 1):
			# no joysticks found
			print "Please connect a joystick.\n"
			self.quit()
		else:
			# create a new joystick object from
			# ---the first joystick in the list of joysticks
			Joy0 = pygame.joystick.Joystick(0)
			# tell pygame to record joystick events
			Joy0.init()

		## bind the event I'm defining to a callback function
		self.root.bind("<<JoyFoo>>", self.my_event_callback)

		## start looking for events
		self.root.after(0, self.find_events)

	def find_events(self):
		## check everything in the queue of pygame events
		events = pygame.event.get()
		for event in events:
			# event type for pressing any of the joystick buttons down
			if event.type == pygame.JOYAXISMOTION:
				# generate the event I've defined
				self.root.event_generate("<<JoyFoo>>")
		## return to check for more events in a moment
		self.root.after(100, self.find_events)

	def my_event_callback(self, event):
		Joy0 = pygame.joystick.Joystick(0)
		# tell pygame to record joystick events
		Joy0.init()
		if Joy0.get_axis(0) != 0:
			if Joy0.get_axis(0) == -1:
				print 'left'
			else:
				print 'right'
		elif Joy0.get_axis(1) != 0:
			if Joy0.get_axis(1) == -1:
				print 'up'
			else:
				print 'down'
		else:
			print 'stop'

  ## quit out of everything
	def quit(self):
		import sys
		sys.exit()




# event handler creates connect thread
def connect_evt():
    t = threading.Thread(target=connect)
    t.daemon = True
    t.start()
    widget_track['connect'].config(text="Connected", state="disabled", command=None)

def connect():
  time.sleep(5)   # todo: temporary for test
  return
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect('192.168.1.2', username='pi', password='raspberry')
  stdin, stdout, stderr = ssh.exec_command('cd')
  stdin, stdout, stderr = ssh.exec_command('roscore &')
  time.sleep(20)
  stdin, stdout, stderr = ssh.exec_command('\n')
  stdin, stdout, stderr = ssh.exec_command('cd scripts')
  stdin, stdout, stderr = ssh.exec_command('python /home/pi/scripts/listener2.py')
  return

# event handler creates run thread
def run_evt():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    widget_track['run'].config(text="Running", state="disabled", command=None)

def run():
  root.bind_all('<KeyPress>', kp)
  print ('foooo')
  #time.sleep(5)     # todo: temporary for test
  #return
  #stdin, stdout, stderr = ssh.exec_command('python ES96_Vivaldi/talker2.py')

def talker(data):
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    pub.publish(data)
    rate.sleep()

def kp(event):
	if event.keysym == 'Up' :
		talker(Front)
	elif event.keysym =='Down' :
		talker(Back)
	elif event.keysym =='Left' :
		talker(Left)
	elif event.keysym =='Right' :
		talker(Right)
	else :
		talker(Stop)

root = Tk()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# connect button starts connect background thread
btn = ttk.Button(mainframe, text="Connect", command=connect_evt)
btn.grid(column=1, row=3, sticky=S)
widget_track['connect'] = btn

# run button start run background thread
btn = ttk.Button(mainframe, text="Run", command=run_evt)
btn.grid(column=3, row=3, sticky=S)
widget_track['run'] = btn

ttk.Label(mainframe, text="Click 'Connect' to establish link.").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Click 'Run' to control using the arrow keys").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()