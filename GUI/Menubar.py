from tkinter import *

window = Tk()


def openFile():
    print("File has been opend")


def saveFile():
    print("File has been saved")


def cut():
    print("cut")


def copy():
    print("copy")


def paste():
    print("paste")


menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0, font=("MV Boli", 15))
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menuBar, tearoff=0, font=("MV Boli", 15))
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_separator()
editMenu.add_command(label="paste", command=paste)

window.geometry('+%d+%d' % (1400, 0))
window.mainloop()
