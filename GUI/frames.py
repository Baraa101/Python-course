from tkinter import *

window = Tk()

frame= Frame(window,bg="pink",bd=5,relief=SUNKEN)
""" frame.pack(side=BOTTOM) """
frame.place(x=0,y=0)
Button(frame,text="W",font=("Consoles",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consoles",25),width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consoles", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consoles", 25), width=3).pack(side=LEFT)

window.geometry('+%d+%d' % (1400, 0))
window.mainloop()