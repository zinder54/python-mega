from tkinter import Tk, Button, Entry, Label, StringVar
import tkinter.ttk as ttk

app =Tk()
app.title("Kiwa site calculations")
app.resizable(0,0)
s=ttk.Style()
app.iconbitmap(r'./Kiwalogo1050x525.ico')
app.geometry("750x300")
s.theme_use("winnative")


def calculation(e1, e2, e3, e4):
    calclabel = Label(text="return calculation",
                     font=("calibri", 16, "bold"),
                     foreground="red",
                     pady=30,
                     padx=10).grid(row=4, column=0, columnspan=3)
    return calclabel

l1 = Label(text="entry box 1",
           font=("calibri", 16),
           pady=30,
           padx=10).grid(row=0, column=0)

l2 = Label(text="entry box 2",
           font=("calibri", 16),
           pady=30,
           padx=10).grid(row=0, column=2)

l3 = Label(text="entry box 3",
           font=("calibri", 16),
           pady=10,
           padx=10).grid(row=1, column=0)

l4 = Label(text="entry box 4",
           font=("calibri", 16),
           pady=10,
           padx=10).grid(row=1, column=2)

entry1 = Entry(app, width=20,
               font=("calibri", 16))
entry1.grid(row=0, column=1)


entry2 = Entry(app, width=20,
           font=("calibri", 16))
entry2.grid(row=0, column=3)

entry3 = Entry(app, width=20,
           font=("calibri", 16))
entry3.grid(row=1, column=1)

entry4 = Entry(app, width=20,
           font=("calibri", 16))
entry4.grid(row=1, column=3)

submit = Button(app,
                width=15,
                text="submit",
                command=lambda: calculation(entry1.get(),
                                            entry2.get(),
                                            entry3.get(),
                                            entry4.get()),
                font=("calibri", 12, "bold"),
                pady=3).grid(row=2, column=3,
                              sticky="E")

app.mainloop()