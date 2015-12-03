from multiprocessing import Process
import sys
from Tkinter import *

main = Tk()



def kp(event):
    if event.keysym == 'Up' :
        p1 = Process(target = func1)
        p2 = Process(target = func2)
        p1.start()
        p2.start()
    else :
        print 'nope'


rocket = 0

def func1():
    global rocket
    print 'start func1'
    while rocket < 5000:
        rocket += 1
        print rocket
    print 'end func1'

def func2():
    global rocket
    print 'start func2'
    while rocket < 5000:
        rocket += 1
        print rocket
    print 'end func2'


main.bind_all('<KeyPress>', kp)
main.mainloop()