from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB=1000
    download=0
    speed=5
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        task.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()


window = Tk()

percent=StringVar()
task=StringVar()

bar =Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10) 

percentLabel=Label(window,textvariable=percent).pack()
taskLabel=Label(window,textvariable=task).pack()

btn=Button(text="Download",command=start).pack()

window.geometry('+%d+%d' % (1400, -400))
window.mainloop()
