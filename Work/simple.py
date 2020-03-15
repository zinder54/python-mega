# import tkinter
#import tkinter as tk
#from tkinter import *
#import tkinter.ttk as ttk

# create the gui app and size of the app
#app = Tk()
##app.title("kiwa barrier testing")
#app.geometry('400x400')

#create a table
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()

height = 5 + 1
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)


#l1 =




mainloop()


#app.mainloop()
