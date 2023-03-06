from tkinter import *

def display():
    if(x.get()==1):
        print("You Agree")
    else:
        print("You do not Agree :(")


window = Tk()

photo = PhotoImage(file='./imgs/like.png')
x = IntVar()
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial",20),
                           fg="#00FF00",
                           bg="#000",
                           activeforeground="#00FF00",
                           activebackground="#000",
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=RIGHT)
check_button.pack()


window.mainloop()