from tkinter import *
import time

from Ball import *

WIDTH = 500
HEIGHT = 500

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

vollyBall = Ball(canvas,0,0,100,1,1,"white")
renisBall = Ball(canvas,0,0,50,4,3,"yellow")
basketBall = Ball(canvas,0,0,100,8,7,"orange")

window.geometry('+%d+%d' % (1400, -600))

while True:
    vollyBall.move()
    renisBall.move()
    basketBall.move()
    window.update()
    time.sleep(0.01)


window.mainloop()
