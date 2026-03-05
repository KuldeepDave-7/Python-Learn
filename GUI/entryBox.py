from tkinter import *

def submit():
    name = entry.get()
    print(name)
   # entry.config(state=DISABLED)

def backspace():
    entry.delete(len(entry.get())-1,END)

def delete():
    entry.delete(0,END)

window = Tk()

# show :- can be used as a substitue for character (in case of writing password you dont want to show the char instead "*")

entry = Entry(window,font=("aerial",52),bg="Black",fg="light green") # show = "*"
#entry.insert(0,"Hello :D")
entry.pack(side=LEFT)

Submit_button = Button(window,text="Submit",command=submit,background="White",activebackground="white",relief=SOLID)
Submit_button.pack(side=RIGHT)

Backspace_button = Button(window,text="Backspace",command=backspace,background="White",activebackground="white",relief=SOLID)
Backspace_button.pack(side=RIGHT)

Delete_button = Button(window,text="Delete",command=delete,background="White",activebackground="white",relief=SOLID)
Delete_button.pack(side=RIGHT)

window.mainloop()