from tkinter import *

food = ["pizza", "burger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a burger!")
    elif(x.get()==2):
        print("You ordered a hotdog!")
    else:
        print("huh?!!")


window = Tk()

pizzaImg = PhotoImage(file="./imgs/pizza.png")
burgerImg = PhotoImage(file="./imgs/burger.png")
hotdogImg = PhotoImage(file="./imgs/hotdog.png")
foodImgs = [pizzaImg,burgerImg,hotdogImg]

x=IntVar()
for i in range(len(food)):
    radioBtn = Radiobutton(window,text=food[i],
    variable=x,
    value=i,
    padx=25,
    font=("Impact",50),
    image=foodImgs[i],
    compound=LEFT,
    indicatoron=0,
    width=375,
    command=order)
    radioBtn.pack(anchor=W)


window.mainloop()
