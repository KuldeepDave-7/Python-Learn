from tkinter import *

def work(event):
   # print("Hey you have done some work")
    label.config(text=event.keysym)
window = Tk()

window.bind("<Key>",work)
label = Label(window,font=("Helvetica",100),width=10)
label.pack()
window.mainloop()

from tkinter import *

def do_something(event):
    print("Your coordinate is "+str(event.x)+" "+str(event.y))

window = Tk()

window.bind("<Button-1>",do_something)

window.mainloop()