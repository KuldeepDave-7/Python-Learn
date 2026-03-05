from tkinter import *

window = Tk()

name = Label(window,text="Enter Your Name",font=("arial",10)).grid(row=0,column=0)
entryname = Entry(window).grid(row=0,column=1)

password = Label(window,text="Enter Password",font=("arial",10)).grid(row=1,column=0)
entrypassw = Entry(window).grid(row=1,column=1)

Button(window,text="Submit").grid(row=2,column=0,columnspan=2)

window.mainloop()