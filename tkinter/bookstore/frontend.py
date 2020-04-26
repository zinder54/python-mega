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
from oopbe import database

Database = database("books.db")

def get_selected_row(event):
    #try:  #<one way below is another
    if lb.curselection():
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple=lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    #except indexerror:
    #    pass


#creates for loop for rows in backend def view function for sqlite3 and inserts
#into Listbox
def view_command(): #creates function to call view function in backend and connect to listbox
    lb.delete(0, END)# deletes any data in the list box before presenting new
    for rows in Database.view(): #creates for loop to go through db and return rows
        lb.insert(END, rows) # inserts the data collected from backend inserts to listbox

def search_command():
    lb.delete(0, END)
    for rows in Database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lb.insert(END, rows)

def add_command():
    Database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lb.delete(0,END)
    lb.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    Database.delete(selected_tuple[0])


def update_command():
    Database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
#tkiner gui

window = Tk()
window.wm_title("BookStore")

l1=Label(window, text="Title")
l1.grid(row=0)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="IBSN")
l4.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1, column=3)

lb=Listbox(window, height=6,width=35)
lb.grid(row=2,column=0,rowspan=6,columnspan=2)
lb.bind('<<ListboxSelect>>', get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

lb.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb.yview)

b1=Button(window, text="view all",width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry",width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Entry",width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window, text="Update",width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete",width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="Close",width=12, command=window.destroy)
b6.grid(row=7,column=3)



window.mainloop()
