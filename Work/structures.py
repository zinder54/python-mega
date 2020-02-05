import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("barrier testing")

tkinter.Label(window, text = "Client").grid(row = 0)
tkinter.Entry(window).grid(row = 1, column = 0)

tkinter.Label(window, text = "Site").grid(row = 0, column = 1)
tkinter.Entry(window).grid(row = 1, column = 1)

tkinter.Label(window, text = "Location").grid(row = 0, column = 2)
tkinter.Entry(window).grid(row = 1, column = 2)

tkinter.Label(window, text = "Date").grid(row = 0, column = 3)
tkinter.Entry(window).grid(row = 1, column = 3)

tkinter.Label(window, text = "Job Reference").grid(row = 0, column = 4)
tkinter.Entry(window).grid(row = 1, column = 4)

tkinter.Label(window, text = "Barrier REF. No.").grid(row = 2, column = 0)
tkinter.Entry(window).grid(row = 2, column = 1)

tkinter.Label(window, text = "SPECIFIED LOAD/m, BEDDING").grid(row = 3, column = 0)
tkinter.Entry(window).grid(row = 3, column = 1)

height  = 10
width = 10
for i in range(height):
    for j in range(width):
        tkinter.Entry(window, text= "comments").grid(row=2, column=2)

window.mainloop()


