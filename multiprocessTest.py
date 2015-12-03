from multiprocessing import Process
import sys
from Tkinter import *

main = Tk()



def kp(event):
    if event.keysym == 'Up' :
        p1 = Process(target = func1,args=(5,))
        p2 = Process(target = func2, args=(13,))
        p1.start()
        p2.start()
    else :
        print 'nope'


rocket = 0

def func1(n):
    global rocket
    print 'start func1'
    while rocket < int(n):
        rocket += 1
        print rocket
    print 'end func1'

def func2(n):
    global rocket
    print 'start func2'
    while rocket < int(n):
        rocket += 1
        print rocket
    print 'end func2'


main.bind_all('<KeyPress>', kp)
main.mainloop()