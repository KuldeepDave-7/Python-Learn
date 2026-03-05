from tkinter import *

def create():
    # First way through which we can create a window
     # new_window = Toplevel()    # Think of it as a top level window which is linked,stack and dependent on the bottom/old window
      new_window = Tk()          # Creates a seprate whole new window which is not dependent on old window
      old_window.destroy()       # Destroy old window upon creation of a new window 
old_window = Tk()
old_window.geometry("220x220")
Button(old_window,text="Create New Window",font=("consolas"),command=create).pack()

old_window.mainloop()