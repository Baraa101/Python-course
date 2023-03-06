from tkinter import *

window = Tk()

def submit():
    print ("The temperature is: "+str(scale.get())+" C")

hot = PhotoImage(file="./imgs/fire.png")
hotlabel=Label(image=hot)
hotlabel.pack()
scale = Scale(window,from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font = ("consolas",20),
              tickinterval=10,
              showvalue=0,
              resolution=5,
              troughcolor='#69EAFF',
              fg="#FF1C00",
              bg="#111")
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()
cold = PhotoImage(file="./imgs/snow.png")
coldlabel=Label(image=cold)
coldlabel.pack()

button = Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()