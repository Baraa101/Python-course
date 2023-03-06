from tkinter import *
from tkinter.ttk import *

window = Tk()

roboot_Movement = Frame(window, width=50)
main_frame = Frame(window, width=50)
floor_status = Frame(window, width=50)


roboot_Movement.grid(column=0, row=0)
main_frame.grid(column=1, row=0)
floor_status.grid(column=2, row=0)


movement_text = Text(roboot_Movement, bg="red")
movement_text.pack()
floor_text = Text(floor_status, bg="red")
floor_text.pack()

for i in range(3):
    for j in range(3):
        Button(main_frame, text="Hello",width=10,height=10).grid(row=i,column=j)


window.mainloop()
