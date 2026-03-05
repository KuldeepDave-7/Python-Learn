# Listbox :- A listing of selectable item within its own container
from tkinter import *

def multisubmit():
        item = []
        for i in listbox.curselection():
                item.insert(i,listbox.get(i))

        print(item)        

def submit():    
        print(listbox.get(listbox.curselection()))

def add():
        listbox.insert(listbox.size(),entry.get())
        listbox.config(height=listbox.size())

def delete():
        f = 0
        l = 0
        for i in listbox.curselection():
            f = i
            break
        for i in listbox.curselection():
               l = i

        listbox.delete(first=f,last=l)               
                  
window = Tk()

listbox = Listbox(window,font=("constantia",30),
                  width=10,bg="light yellow",fg="black",selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Sphagetti")
listbox.insert(3,"Salad")
listbox.insert(4,"Coffee")
listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

button = Button(window,text="Submit",command=multisubmit,font=("consolas",12,"bold"),bg="light yellow")
button.pack()

addbutton = Button(window,text="Add",command=add,font=("consolas",12,"bold"),bg="light yellow")
addbutton.pack()

delete_button = Button(window,text="Delete",command=delete,font=("consolas",12,"bold"),bg="light yellow")
delete_button.pack()
window.mainloop()