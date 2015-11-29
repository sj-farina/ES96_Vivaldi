#python 3
#from tkinter import *
#from tkinter import ttk

#python 2
from Tkinter import *
import ttk

import time
import subprocess
import paramiko

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


def connect():
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect('192.168.1.2', username='pi', password='raspberry')
  stdin, stdout, stderr = ssh.exec_command('echo foo')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('cd')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('roscore &')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('cd scripts')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('echo raspberry | sudo -S su')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('python /home/pi/scripts/listener2.py')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()



root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Button(mainframe, text="Connect", command=connect).grid(column=1, row=3, sticky=S)
#ttk.Button(mainframe, text="Connect2", command=connect2).grid(column=2, row=3, sticky=S)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()