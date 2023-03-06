# Imports and initalization
import tkinter
from tkinter import Canvas

window = tkinter.Tk()
c = Canvas(window, width=300, height=300)
c.pack()
x0 = 0
y0 = 0
x1 = 50
y1 = 50
color = "red"
for i in range(6):
    for j in range(6):
        c.create_rectangle(x0, y0, x1, y1, fill=color)
        if color == "red":
            color = "green"
        else:
            color = "red"
        x0 += 50
        x1 += 50
    if color == "red":
        color = "green"
    else:
        color = "red"
    x0 = 0
    x1 = 50
    y0 += 50
    y1 += 50


window.mainloop()
