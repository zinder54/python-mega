from tkinter import * #imports all tkinter modules

app = Tk() #creates the app/window

def KMtoMiles(): #function to format button action
    miles=float(E1Value.get())*0.6 #turn string into float and x 0.6
    t1.insert(END, miles) #inserts miles into text box

b1 = Button(app, text="execute", command=KMtoMiles) #creates a button with text, always start with link to app
b1.grid(row=0) #puts button into grid system.        ##and adds in command to get function of button

E1Value = StringVar() #get the value from the entry widget
e1 = Entry(app, textvariable=E1Value)
e1.grid(row=0,column=1) #same as above but with entry

t1 = Text(app, height=1, width=20) #as above
t1.grid(row=0,column=2)

app.mainloop() #has to be in so app stay open till x is clicked
