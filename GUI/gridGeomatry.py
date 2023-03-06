from tkinter import *

window = Tk()

titleLabel =Label(text="Enter some info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

fnameLabel = Label(window, text="First Name: ", width=20,
                   bg="red").grid(row=1, column=0)
fNameEntry = Entry(window).grid(row=1, column=1)

lnameLabel = Label(window, text="Last Name: ",
                   bg="green").grid(row=2, column=0)
lNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="Email: ", bg="blue",
                   width=30).grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(
    row=4, column=0, columnspan=2)

window.geometry('+%d+%d' % (1400, 300))
window.mainloop()
