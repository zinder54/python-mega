from tkinter import *
from tkinter import Tk, Button, Entry, Label, StringVar
import tkinter.ttk as ttk

app = Tk()
app.title("Kiwa site calculations")
app.resizable(0, 0)
s = ttk.Style()
app.geometry("750x300")
s.theme_use("winnative")


L1 = Label(app, text="Client",
           pady=15,
           padx=10).grid(row=0)
E1 = Entry(app).grid(row=1, column=0)

L2 = Label(app, text = "Site",
           pady=15,
           padx=30).grid(row=0, column=1)
E2 = Entry(app).grid(row=1, column=1)

L3 = Label(app, text="Location",
           pady=15,
           padx=30).grid(row = 0, column = 2)
E3 = Entry(app).grid(row=1, column=2)

L4 = Label(app, text="Job REF.",
           pady=15,
           padx=30).grid(row=0, column=3)
E4 = Entry(app).grid(row=1, column=3)

L5 = Label(app, text="DATE",
           pady=15,
           padx=30).grid(row=0, column=4)
E5 = Entry(app).grid(row=1, column=4)

L6 = Label(app, text="barrier REF. No.",
           pady=5,
           padx=0).grid(row=3)
E6 = Entry(app).grid(row=3, column=1)

L7 = Label(app, text="Specified load/m(Bedding)",
           pady=5,
           padx=0).grid(row=4)
E7 = Entry(app).grid(row=4, column=1)
L7a = Label(app, text="Kn/m",
            pady=0,
            padx=0).grid(row=4, column=2)


#height  = 10
#width = 10
#for i in range(height):
 #   for j in range(width):
  #      tkinter.Entry(app, text= "comments").grid(row=2, column=2)

app.mainloop()


