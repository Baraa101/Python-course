from tkinter import *


def doSomething(event):
    label.config(text=event.keysym)

window = Tk()

window.bind("<Return>",doSomething)
window.bind("<q>",doSomething)
window.bind("<Key>",doSomething)

label =Label(window,font=("Helvetica",100))
label.pack()

window.geometry('+%d+%d' % (1400, -500))
window.mainloop()
