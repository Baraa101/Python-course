from tkinter import *

window = Tk()

def submit():
    orders = [];
    for i in (listBox.curselection()):
        orders.insert(i,listBox.get(i))
    print("You have ordered: ")
    for i in (orders):
        print(i)
    """ print(listBox.get(listBox.curselection())) """

def add():
    listBox.insert(listBox.size(),entryBox.get())
    listBox.config(height=listBox.size())

def delete():
    """ listBox.delete(listBox.curselection()) """
    for i in reversed(listBox.curselection()):
        listBox.delete(i)
    listBox.config(height=listBox.size())

listBox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listBox.pack()

listBox.insert(1, "Pizza")
listBox.insert(2, "Pasta")
listBox.insert(3, "Garlic bread")
listBox.insert(4, "Soup")
listBox.insert(5, "Salad")

listBox.config(height=listBox.size())

entryBox= Entry(window)
entryBox.pack()

submitBtn = Button(window,text="Submit",command=submit)
submitBtn.pack()

addBtn = Button(window,text="Add",command=add)
addBtn.pack()

deleteBtn = Button(window,text="Delete",command=delete)
deleteBtn.pack()

window.geometry('+%d+%d' % (1400, 0))
window.mainloop()
