from tkinter import *
from time import strftime

def update():
    time = strftime("%I:%M:%S")
    time_label.config(text=time)
    
    month = strftime("%b %d, %y")
    month_label.config(text=month)

    day = strftime("%A")
    day_label.config(text=day)  

    window.update()
    window.after(1000,update)

window = Tk()

canvas  = Canvas(window,width=300,height=200,bg="black")
canvas.pack()

month_label = Label(canvas,font=("san seriff",30),fg="#00FFFF",bg="black")
time_label = Label(canvas,font=("san seriff",50),fg="#00FFFF",bg="black")
day_label = Label(canvas,font=("san seriff",20),fg="#00FFFF",bg="black")

canvas.create_window(150,40,window=month_label)
canvas.create_window(150,110,window=time_label)
canvas.create_window(150,170,window=day_label)

update()
window.mainloop()