#!/usr/bin/env python3

from tkinter import *
import subprocess
import threading

root = Tk()
root.title('WiFi Zom')
root.geometry('400x200+100+100')

z = StringVar()

w = Message(root, textvariable=z, width=200, bg='#ededed', anchor=NW, font='Source-Code-Pro 12')
w.pack(fill=BOTH, expand=1, side=LEFT)

opt_val = StringVar()
opt_val.set('fr1777')

opts = OptionMenu(root, opt_val, 'fr1777', 'lolis-fr888')
opts.pack(side=TOP)

def connect_wifi():
    ap = opt_val.get()
    cmd = 'sudo /home/ginetom/dev/wifi-zom/wifi ' + ap
    x = threading.Thread(target=run_process, args=(cmd,))
    x.start()
    return

def disconnect():
    cmd = 'sudo /home/ginetom/dev/wifi-zom/wifi down'
    x = threading.Thread(target=run_process, args=(cmd,))
    x.start()
    return

def run_process(cmd):
    process = subprocess.Popen(cmd.split(),
        stdout=subprocess.PIPE, universal_newlines=True)

    with process as p:
        message = ''
        for line in p.stdout:
            message += line + "\n"
            z.set(message)

b = Button(root, text='Connect', command=connect_wifi)
b.pack(side=RIGHT)

b = Button(root, text='Disconnect', command=disconnect)
b.pack(side=RIGHT)

root.mainloop()


