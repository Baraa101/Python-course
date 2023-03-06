from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

ufoImg = PhotoImage(file='./imgs/ufo.png')
spaceImg = PhotoImage(file='./imgs/space.png')

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background = canvas.create_image(0, 0, image=spaceImg, anchor=NW)
ufo = canvas.create_image(0, 0, image=ufoImg, anchor=NW)

window.geometry('+%d+%d' % (1400, -600))

running = TRUE

imgWidth = ufoImg.width()
imgHeight = ufoImg.height()

while running:
    cords = canvas.coords(ufo)
    if (cords[0] >= (WIDTH-imgWidth) or cords[0] < 0):
        xVelocity *= (-1)
    if (cords[1] >= (HEIGHT-imgHeight) or cords[1] < 0):
        yVelocity *= (-1)
    canvas.move(ufo, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()
