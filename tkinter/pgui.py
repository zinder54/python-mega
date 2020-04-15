from tkinter import *

app = Tk()

def converter():
    grams=float(E1VALUE.get())*1000
    pounds=float(E1VALUE.get())*2.20462
    ounces=float(E1VALUE.get())*35.274
    t1.delete("1.0", END) #deletes previous entries for fresh convert
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)


l1 = Label(app, text="Kg")
l1.grid(row=0)

E1VALUE = StringVar()
e1 = Entry(app,textvariable=E1VALUE)
e1.grid(row=0, column=1)

t1 = Text(app, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(app, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(app, height=1, width=20)
t3.grid(row=1, column=2)

b1 = Button(app, text="Convert", command=converter)
b1.grid(row=0, column=2)

app.mainloop()
