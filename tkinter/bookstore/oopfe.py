from tkinter import *

#imports backend py file
from oopbe import database

Database = database("books.db")

class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("BookStore")
        l1=Label(window, text = "Title")
        l1.grid(row=0,column=0)

        l2=Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3=Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4=Label(window, text="IBSN")
        l4.grid(row=1, column=2)

        self.title_text=StringVar()
        self.e1=Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text=StringVar()
        self.e2=Entry(window,textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text=StringVar()
        self.e3=Entry(window,textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.lb=Listbox(window, height=6,width=35)
        self.lb.grid(row=2,column=0,rowspan=6,columnspan=2)
        self.lb.bind('<<ListboxSelect>>', self.get_selected_row)

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2, rowspan=6)

        self.lb.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.lb.yview)

        b1=Button(window, text="view all",width=12, command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window, text="Search Entry",width=12, command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window, text="Add Entry",width=12, command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window, text="Update",width=12, command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window, text="Delete",width=12, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window, text="Close",width=12, command=window.destroy)
        b6.grid(row=7,column=3)

    def get_selected_row(self,event):#has to be within the class to be attributed
        if self.lb.curselection():
            index=self.lb.curselection()[0]#dont need global variable because of self
            self.selected_tuple =self.lb.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
    #except indexerror:
    #    pass
    def view_command(self): #creates function to call view function in backend and connect to listbox
        self.lb.delete(0, END)# deletes any data in the list box before presenting new
        for rows in Database.view(): #creates for loop to go through db and return rows
            self.lb.insert(END, rows) # inserts the data collected from backend inserts to listbox

    def search_command(self):
        self.lb.delete(0, END)
        for rows in Database.search(self.title_text.get(),self.author_text.get(),
                                    self.year_text.get(),self.isbn_text.get()):
            self.lb.insert(END, rows)

    def add_command(self):
        Database.insert(self.title_text.get(),self.author_text.get(),
                        self.year_text.get(),self.isbn_text.get())
        self.lb.delete(0,END)
        self.lb.insert(END,(self.title_text.get(),self.author_text.get(),
                            self.year_text.get(),self.isbn_text.get()))

    def delete_command(self):
        Database.delete(self.selected_tuple[0])

    def update_command(self):
        Database.update(self.selected_tuple[0],self.title_text.get(),
                        self.author_text.get(),self.year_text.get(),self.isbn_text.get())


window = Tk()
Window(window)#calls the function and class
window.mainloop()
