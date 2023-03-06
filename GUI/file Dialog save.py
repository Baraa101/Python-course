from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(
        initialdir="H:/Top/Codeing/2023 part 1/Python/GUI/files",
        defaultextension=".txt",
        filetypes=[
        ("Text file",".txt"),
        ("HTML file",".html"),
        ("All files",".*"),
        ])
    if file is None:
        return
    fileText = str(text.get(1.0, END))
    file.write(fileText)
    file.close()

window = Tk()

btn=Button(text="save",command=saveFile)
btn.pack()
text =Text(window)
text.pack()
window.geometry('+%d+%d' % (1400, 0))
window.mainloop()
