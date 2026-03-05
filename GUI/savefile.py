from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[
            ("Text file",".txt"),
            ("Html file",".html"),
            ("all files",".*")
          ])
    if file is None:
         return
    filetext = text.get(1.0,END) 
    #filetext = input("Enter Text to save: ")
    file.write(filetext)
    file.close()

window = Tk()

button = Button(window,text="Save",command=savefile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()