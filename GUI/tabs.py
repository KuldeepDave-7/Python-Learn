from tkinter import *
from tkinter import ttk

window = Tk()

book = ttk.Notebook(window)    # used to create tabbed interfaces in  GUI

tab1 = Frame(book,bd=5,relief=SUNKEN)
tab2 = Frame(book)

book.add(tab1, text="Tab1")
book.add(tab2, text="Tab2")
book.pack()
# book.pack(expand=True,fill="both")  expandsto fill any space that is not otherwise using both expand and fill

Label(tab1,text="Hello You are currently on Tab 1 :)",width=55,height=10).pack()
Label(tab2,text="You dont wanna be on Tab 1 why ? :(",width=55,height=10).pack()

window.mainloop()