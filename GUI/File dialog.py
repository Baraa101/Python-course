from tkinter import *
from tkinter import filedialog

def openFile():
    filePath = filedialog.askopenfilename(
        initialdir="H:/Top/Codeing/2023 part 1/Python/GUI",
        title="Open File",
        filetypes=(("text files","*.txt"),("all files","*.*")))
    file = open(filePath, 'r')
    print(file.read())
    file.close()

window = Tk()
btn = Button(text="File",command=openFile)
btn.pack()




window.geometry('+%d+%d' % (1300, 0))
window.mainloop()
