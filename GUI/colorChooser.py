from tkinter import *
from tkinter import colorchooser


def click():
    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("420x420")
button = Button(text="Click", command=click)
button.pack()


window.geometry('+%d+%d' % (1400, 0))
window.mainloop()
