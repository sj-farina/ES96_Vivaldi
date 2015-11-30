#python 3
#from tkinter import *
#from tkinter import ttk

#python 2
from Tkinter import *
import ttk

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
  time.sleep(5)     # todo: temporary for test
  return
  stdin, stdout, stderr = ssh.exec_command('python ES96_Vivaldi/talker2.py')


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