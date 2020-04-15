"""
a programme that stores book information:
Title, Author
Year, Isbn

user can:

view all data
add data
update data
delete data
close
"""
from tkinter import *

#imports backend py file
import backend

#creates for loop for rows in backend def view function for sqlite3 and inserts
#into Listbox
def view_command():
    lb.delete(0, END)
    for rows in backend.view():
        lb.insert(END, rows)

def search_comman():
    lb.delet(0, END)
    for rows in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lb.insert(END, rows)
#tkiner gui

window = Tk()

l1=Label(window, text="Title")
l1.grid(row=0)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="IBSN")
l4.grid(row=1, column=2)

title_text=StringVar
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar
e2=Entry(window,textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar
e3=Entry(window,textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1, column=3)

lb=Listbox(window, height=6,width=35)
lb.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

lb.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb.yview)

b1=Button(window, text="view all",width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry",width=12)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Entry",width=12)
b3.grid(row=4,column=3)

b4=Button(window, text="Update",width=12)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete",width=12)
b5.grid(row=6,column=3)

b6=Button(window, text="Close",width=12)
b6.grid(row=7,column=3)



window.mainloop()
