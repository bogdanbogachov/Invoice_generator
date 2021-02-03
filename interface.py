from tkinter import *

root = Tk() # standard beginning

myLabel1 = Label(root, text = """Enter customer's name and
last name as in Google Calendar:""") # label creation
myLabel1.grid(row = 0, column = 0) # label positioning

e = Entry(root, width = 50, bg = "white", borderwidth = 5) # entry field creation
e.grid(row = 0, column = 1) # entry field positioning

customer = None

def name(): # a function which is called when pressing a button
    global customer # lets me change the customer variable from the global frame
    customer = e.get()
    root.destroy() # closes Tkinter window after button is clicked

mybutton = Button(root, text = "Create an invoice", command = name) # button creation
mybutton.grid(row = 1, column = 1) # button positioning

root.mainloop() # standard ending