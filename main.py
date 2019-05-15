#!/usr/bin/env python3

from tkinter import *
import subprocess
import threading

root = Tk()
root.title('WiFi Zom')
root.geometry('400x200+100+100')

z = StringVar()

w = Message(root, textvariable=z, width=200, bg='#ededed', anchor=NW, font='Menlo 12')
w.pack(fill=BOTH, expand=1, side=LEFT)

opt_val = StringVar()
opt_val.set('fr777')

opts = OptionMenu(root, opt_val, 'fr777', 'ale-hotspot')
opts.pack(side=TOP)

def connect_wifi():
    x = threading.Thread(target=run_process)
    x.start()
    return

def run_process():
    ap = opt_val.get()
    # TODO provide access point to command
    cmd = './wifi up ale'
    process = subprocess.Popen(cmd.split(),
        stdout=subprocess.PIPE, universal_newlines=True)

    with process as p:
        message = ''
        for line in p.stdout:
            message += line + "\n"
            z.set(message)

b = Button(root, text='Connect', command=connect_wifi)
b.pack(side=RIGHT)

root.mainloop()


