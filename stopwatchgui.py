import tkinter as tkinter
import tkinter.font as TkFont
from datetime import datetime

def run():
    current_time = datetime.now()
    diff = current_time - start_time
    txt.var.set('%d.%02d' % (diff.seconds,diff.microseconds//10000))

    if running:
        root.after(20,run) #to reschedule after 20ms


def start():
    global running
    global start_time

    if not running:
        running = True
        start_time = datetime.now()
        root.after(10,run)

def stop():
    global running
    running = False
    end_time = datetime.now()

def reset():
    global start_time
    start_time = datetime.now()

    if not running():
        txt_var.set('0.00')

running = False
start_time = None