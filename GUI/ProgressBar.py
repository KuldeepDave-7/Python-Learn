from tkinter import *
from tkinter.ttk import *
import time

def downloading():
   Gb = 100
   speed = 2
   download = 0

   while(download < Gb):
      time.sleep(0.05)
      progress['value'] += (speed/Gb)*100
      download += speed
      percent.set(str(int((download/Gb)*100))+" % Downloaded")
      window.update_idletasks()

window = Tk()

percent = StringVar()

progress = Progressbar(window,length=300)
progress.pack()

label =Label(window,font="arial",textvariable=percent)
label.pack()

button = Button(window,text="Download",command=downloading)
button.pack()

window.mainloop()