from tkinter import *

def display():
    if(K.get() == 1):
        print("You Agree !")
    else:
        print("You dont agree :(")    

window = Tk()

K = IntVar()
pic = PhotoImage(file="GUI/download.png")
check_button = Checkbutton(window, text="Do you agree!",font=("arial",30),variable=K,
                           command=display,bg="black",fg="green",activebackground="black",activeforeground="green",
                           padx=30,pady=20,image=pic,compound=LEFT)
check_button.pack()

window.mainloop()