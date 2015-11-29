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
  time.sleep(20)
  stdin, stdout, stderr = ssh.exec_command('\n echo foooooooooo')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('cd scripts')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('python /home/pi/scripts/listener2.py &')
  print "stdout: ", stdout.readlines()
  print "stderr: ", stderr.readlines()
  stdin, stdout, stderr = ssh.exec_command('\n echo done')
  return
def run():
  stdin, stdout, stderr = ssh.exec_command('python ES96_Vivaldi/talker2.py')


root = Tk()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Connect", command=connect).grid(column=1, row=3, sticky=S)
ttk.Button(mainframe, text="Run", command=run).grid(column=3, row=3, sticky=S)

ttk.Label(mainframe, text="Click 'Connect' to establish link.").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="Click 'Run' to control using the arrow keys").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()
