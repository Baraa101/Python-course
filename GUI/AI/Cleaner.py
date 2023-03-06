# Imports and initalization
from tkinter import *
import time
from Vacum import *
import threading
import random
import tkinter.scrolledtext as scrolledtext

WIDTH = 400
HEIGHT = 200


class Location:
    def __init__(self, rect, symbol):
        self.rect = rect
        self.clean = True
        self.symbol = symbol


window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)

locationA = Location(canvas.create_rectangle(
    0, 0, 200, 200, fill="Green"), 'A')
locationB = Location(canvas.create_rectangle(
    200, 0, 400, 200, fill="Green"), 'B')


enviromentState = scrolledtext.ScrolledText(
    window,
    bg="black",
    width=20,
    height=30,
    fg="white")
vcState = scrolledtext.ScrolledText(
    window,
    bg="black",
    width=20,
    height=30,
    fg="white")
performanceValue = scrolledtext.ScrolledText(
    window,
    bg="black",
    width=48,
    height=12,
    fg="white")

""" timer = Text(window, width=25, height=5, font=(
    "Baskerville Old Face", 50), bg='black', fg='#00FF00') """

vacum = Vacum(canvas, window, 100, 5, "pink", locationA, locationB, vcState)
timerFrame = Frame(window)
timer = Label(timerFrame, width=8, font=(
    "Baskerville Old Face", 50), bg='black', fg='#00FF00')
resetBtn = Button(timerFrame, text="R", height=5,
                  width=11, bg='black', fg='#00FF00')
timer.pack(side=LEFT)
resetBtn.pack(side=RIGHT)

enviromentState.grid(column=0, row=0, rowspan=3)
canvas.grid(column=1, row=1)
timerFrame.grid(column=1, row=0)
vcState.grid(column=2, row=0, rowspan=3)
performanceValue.grid(column=1, row=2)


def move():
    startTime = time.time()
    global endTime
    if (startTime < endTime):
        threading.Timer(2.0, move).start()
    else:
        print("Done!")
    vacum.precept()


def dirt():
    startTime = time.time()
    global endTime
    if (startTime < endTime):
        threading.Timer(3.0, dirt).start()
    a = random.randint(0, 1)
    if (a == 0 and locationA.clean):
        locationA.clean = False
        canvas.itemconfig(locationA.rect, fill='red')
    a = random.randint(0, 1)
    if (a == 0 and locationB.clean):
        locationB.clean = False
        canvas.itemconfig(locationB.rect, fill='red')
    enviromentState.insert(
        END, "A: "+("clean"if locationA.clean else "dirty")+"\n")
    enviromentState.insert(END, "B: "+("clean" if locationB.clean else "dirty") +
                           "\n<><><><><><><>\n")
    enviromentState.see("end")


points = 0


def preformanceMesuare():
    global endTime
    startTime = time.time()
    if (startTime < endTime):
        threading.Timer(15.0, preformanceMesuare).start()
    global points
    if (locationA.clean and locationB.clean):
        points += 2
        performanceValue.insert(
            'end', "Points: 2")
    elif (locationA.clean or locationB.clean):
        points += 1
        performanceValue.insert(
            'end', "Points: 1")
    else:
        performanceValue.insert(
            'end', "Points: 0")
    performanceValue.insert(
        'end', "\nTotal: "+str(points)+"\n<><><><><><><>\n")
    performanceValue.see("end")


def run():
    threading.Timer(2.0, move).start()
    threading.Timer(3.0, dirt).start()
    threading.Timer(15.0, preformanceMesuare).start()


timerThread = threading


def timerr():
    timeSet = 60
    while (timeSet >= 0):
        """ timer.delete('1.0', END)
        timer.insert('1.0', str(timeSet)) """
        timer.config(text=str(timeSet))
        timeSet -= 1
        time.sleep(1)


timerThread = threading.Thread(target=timerr)
timerThread.start()
startTime = time.time()
endTime = startTime + 60
run()


window.mainloop()

""" vacum.moveUp() """

""" canvas.create_rectangle(0, 200, 201, 400, fill="Green") """
