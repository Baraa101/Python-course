from tkinter import *

speed = 10


def moveUp(event):
    canvas.move(myCar,0,-speed)


def moveDown(event):
    canvas.move(myCar, 0, speed)


def moveLeft(event):
    canvas.move(myCar, -speed, 0)


def moveRight(event):
    canvas.move(myCar, speed, 0)


window = Tk()

window.bind("<w>", moveUp)
window.bind("<s>", moveDown)
window.bind("<a>", moveLeft)
window.bind("<d>", moveRight)
window.bind("<Up>", moveUp)
window.bind("<Down>", moveDown)
window.bind("<Left>", moveLeft)
window.bind("<Right>", moveRight)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

car = PhotoImage(file='./imgs/car.png')

myCar = canvas.create_image(0, 0, image=car,anchor=NW)

window.geometry('+%d+%d' % (1400, -600))
window.mainloop()
