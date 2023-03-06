from tkinter import *

window = Tk()

cannvas = Canvas(window, height=500, width=500)

""" cannvas.create_line(0, 0, 500, 500, fill="blue", width=5)
cannvas.create_line(0, 500, 500, 0, fill="red", width=5) """
""" cannvas.create_rectangle(50, 50, 250, 250, fill="green", width=5) """
""" points = [250, 0, 500, 500, 0, 500]
cannvas.create_polygon(points, fill="green", outline="black",width=5) """
""" cannvas.create_arc(0,0,500,500, fill="red", outline="black",style=PIESLICE,start=90) """
cannvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=10)
cannvas.create_arc(0, 0, 500, 500, fill="white",
                   extent=180, width=10, start=180)
cannvas.create_oval(190, 190, 310, 310, fill="white", width=10)

cannvas.pack()

window.geometry('+%d+%d' % (1300, -800))
window.mainloop()
