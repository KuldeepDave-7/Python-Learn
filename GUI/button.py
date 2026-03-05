from tkinter import *

# button :- You click it and it perfroms specified task
count = 0
def click():
    global  count
    count += 1
    print("You Cliked Button "+str(count)+" Times")

window = Tk()
# state :- through this you can choose whether to disable the button or in ACTIVE state
# Command :- lets us perform tasks through button when we click
# Compound :- lets us choose whether to place the image left,right,top,bottom

Photo = PhotoImage(file='GUI/download.png')
button = Button(window,text="Click Here !",command=click,font=("comic sans",30,'bold'),
                fg="#00FF00",background='black',activeforeground="#00FF00",activebackground='black',state=ACTIVE,
                image=Photo,compound=BOTTOM)

button.pack()

window.mainloop()