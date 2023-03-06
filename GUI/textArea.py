from tkinter import *


def submit():
    input = textArea.get("1.0", END)
    print(input)


window = Tk()

textArea = Text(window,
                bg="light yellow",
                font=("Ink Free", 25),
                height=8,
                width=20, padx=20, pady=20,
                fg="purple")
textArea.pack()

btn = Button(window, text="Submit", command=submit)
btn.pack()

window.geometry('+%d+%d' % (1300, 0))
window.mainloop()
