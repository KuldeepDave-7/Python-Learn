# filemenu = Menu(menubar, tearoff=0) create a new menu (dropdown) named filemenu,and attach it to the main menubar.
# menubar.add_cascade(label="File", menu=filemenu) add button on the menubar called File,when the user clicks it, open the dropdown filemenu

from tkinter import *

def save():
    print("Your file has been saved")

def edit():
    print("Your file has been edited")

def share():
    print("You have shared one document") 

window = Tk()
window.geometry("420x420")
menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0,font=("MV boli",15))
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Save",command=save)
filemenu.add_command(label="Edit",command=edit)
filemenu.add_separator()
filemenu.add_command(label="Share",command=share)

editmenu = Menu(menubar,tearoff=0,font=("MV boli",15))                   # Creates and attaches it to menubar
menubar.add_cascade(label="Edit",menu=editmenu)      # adds 

editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
window.mainloop()
