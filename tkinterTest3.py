# tkinterTest3.py
# Janey Farina, Alex Raun
# To be run with listener2.py or DriveTheRobot5.py

#This program creates a front end Graphical User Interface
#pressing connect sets up the connection with the Pi
#pressing run allows keypresses to be capturesd and transmitted



#uncomment for python 3
#from tkinter import *
#from tkinter import ttk

#uncomment for python 2
from Tkinter import *
import ttk

import rospy
from std_msgs.msg import Int64
import time
import subprocess
import paramiko

import threading

# keep track of widgets for event handlers
widget_track = {}

# event handler creates connect thread
def connect_evt():
    t = threading.Thread(target=connect)
    t.daemon = True
    t.start()
    widget_track['connect'].config(text="Connected", state="disabled", command=None)

#connects to Pi over ssh, logs in, starts roscore and starts listening program
def connect():
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

# on clicking run, start listening for keypresses
def run():
  root.bind_all('<KeyPress>', kp)

# send keypresses to listener 
def talker(data):
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rospy.loginfo(data)
    pub.publish(data)
    rate.sleep()

# listen for and process key presses
def kp(event):
	if event.keysym == 'Right' :
		talker(18)
	elif event.keysym =='Left' :
		talker(17)
	else :
		talker(0)

root = Tk()

# setting up the GUI window
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
