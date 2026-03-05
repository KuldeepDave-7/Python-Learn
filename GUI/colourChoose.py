from tkinter import *
from tkinter import colorchooser    # submodule

def click():
   colour =  colorchooser.askcolor() 
   window.config(bg=colour[1])

window = Tk()
window.geometry("520x520")

button = Button(window,text="Click", command=click)
button.pack()
window.mainloop()
