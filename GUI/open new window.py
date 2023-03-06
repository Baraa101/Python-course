from tkinter import *

window = Tk()


def create_window():
    """ new_window =Toplevel() """
    new_window =Tk()

    window.destroy()

Button(window,text="create a new window",command=create_window).pack()

window.geometry('+%d+%d' % (1400, 0))
window.mainloop()
