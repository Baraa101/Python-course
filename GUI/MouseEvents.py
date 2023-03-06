from tkinter import *

def doSomething(event):
    print("You did something "+str(event.x)+","+str(event.y))

window = Tk()

#window.bind("<Button-1>",doSomething) #left Click
#window.bind("<Button-2>",doSomething) #scrool Click
#window.bind("<Button-3>",doSomething) #right Click
#window.bind("<ButtonRelease>",doSomething)
#window.bind("<Enter>",doSomething)
#window.bind("<Leave>",doSomething)
window.bind("<Motion>",doSomething)

window.mainloop()