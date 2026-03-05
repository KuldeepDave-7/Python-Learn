from tkinter import *

def submit():
    name  = text.get("1.0",END)
    print(name)

window = Tk()

text = Text(window,bg="light yellow",font=("Ink Free",20),height=8,width=20,
            padx=20,pady=20,fg="maroon")
text.pack()

button = Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()