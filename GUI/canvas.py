from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)

canvas.create_polygon(250,0,0,500,500,500,fill="Red",outline="Black",width=8)

canvas.pack()
window.mainloop()