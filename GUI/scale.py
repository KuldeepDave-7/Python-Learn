from tkinter import *

def submit():
    print("The temperature is "+str(scale.get())+" degree C")

window = Tk()


#window.geometry("520x520")
# scale.set(100) :- sets the knob on scale to 100 default
# resolution :- increment of slider
#showvalue=0 :- hides the current value
scale = Scale(window, from_=0, to=100,
              length=500, orient=VERTICAL,font=("consolas",25),
              tickinterval=10,troughcolor="red",
              bg="black",fg="white",activebackground="black") 
scale.pack()

button = Button(window,text="SUBMIT",command=submit)
button.pack()


window.mainloop()