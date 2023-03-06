from tkinter import *


count=0
def click():
    global count
    count+=1
    print(count)


window = Tk()
photo = PhotoImage(file='./imgs/like.png')
button = Button(window,
                text='do not',
                command=click,
                font=('Comic Sans', 30),
                fg='#00FF00',
                bg='white',
                activeforeground='#00FF00',
                activebackground='white',
                state=ACTIVE,
                image=photo,
                compound='bottom',)
button.pack()
window.mainloop()
