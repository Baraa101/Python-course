from tkinter import *
# widgets = GUI elements: buttons, textboxes, labels, images
# windows serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
""" window.geometry("420x420") """
window.title("First GUI")
photo = PhotoImage(file='./imgs/witcher.png')
label = Label(window,
              text="Hello There!",
              font=('Arial', 40, 'bold'),
              fg='#00FF00', bg='grey',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
""" label.place(x=100,y=100) """


icon = PhotoImage(file='witcher.png')
window.iconphoto(True, icon)
window.config(background='#34568B')

window.mainloop()  # place window on screen, listen to events
