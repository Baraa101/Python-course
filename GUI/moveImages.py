from tkinter import *

speed=10
def moveUp(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-speed)
def moveDown(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+speed)
def moveLeft(event):
    label.place(x=label.winfo_x()-speed, y=label.winfo_y())
def moveRight(event):
    label.place(x=label.winfo_x()+speed, y=label.winfo_y())

window = Tk()

window.bind("<w>",moveUp)
window.bind("<s>",moveDown)
window.bind("<a>",moveLeft)
window.bind("<d>",moveRight)
window.bind("<Up>",moveUp)
window.bind("<Down>",moveDown)
window.bind("<Left>",moveLeft)
window.bind("<Right>",moveRight)

car = PhotoImage(file="./imgs/car.png")
label = Label(window,image=car)
label.place(x=0,y=0)

window.geometry('%dx%d+%d+%d' % (500,500,1300, -600))
window.mainloop()
