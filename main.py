#!/usr/bin/env python3

from tkinter import *
import subprocess
import threading

root = Tk()
root.title('WiFi Zom')
root.geometry('250x250+100+100')

z = StringVar()

w = Label(root, textvariable=z)
w.pack(side=LEFT)

#t = Text(w, state=DISABLED)
#t.pack(side=LEFT)

def connect_wifi():
    x = threading.Thread(target=run_process)
    x.start()
    return

def run_process():
    cmd = './wifi up ale'
    process = subprocess.Popen(cmd.split(),
        stdout=subprocess.PIPE, universal_newlines=True)
    
    with process as p:
        for line in p.stdout:
            z.set(line)
    

b = Button(root, text='Connect to Ale', command=connect_wifi)
b.pack(side=RIGHT)

root.mainloop()


