#Frames :- a regtangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="maroon",relief=RAISED,bd=7)
frame.place(x=0,y=0)

Button(frame,text="I",font=("consolas",15),width=5).pack(side=TOP)
Button(frame,text="J",font=("consolas",15),width=5).pack(side=LEFT)
Button(frame,text="K",font=("consolas",15),width=5).pack(side=LEFT)
Button(frame,text="L",font=("consolas",15),width=5).pack(side=LEFT)

window.mainloop()