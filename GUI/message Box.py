from tkinter import *
from tkinter import messagebox

window = Tk()


def click():
    """ messagebox.showinfo(title="This is an info message",message="You are a wizard") """
    """ messagebox.showwarning(title="WARNING!",message="you have A VAIRUS ! ! ! !") """
    """ messagebox.showerror(title="ERROR!",message="Something went wrong") """
    """ if messagebox.askokcancel(title="ask ok cancel",message="Do you want to?"):
        print("You did it")
    else:
        print("You cancelled") """
    """ if messagebox.askretrycancel(title="ask retry cancel",
                                 message="Retry?"):
        print("You did it")
    else:
        print("You cancelled") """
    """ if messagebox.askyesno(title="Yes/No",
                                 message="Yes?"):
        print("Yes")
    else:
        print("No :(") """
    """ print(messagebox.askquestion(
        title="Ask question", message="Do you like coding?")) """
    print(messagebox.askyesnocancel(
        title="Yes/No/Cncel", message="Do you play the witcher", icon="info"))


button = Button(window, command=click, text="Click Me")
button.pack()

window.mainloop()
