from tkinter import *

def Print():
    if(x.get()==0):
        print("Nice Choice BWM huh ")
        print
    elif(x.get()==1):
        print("Heavy Bike though :)")
    elif(x.get()==2):
        print("Enjoy your ride :D")
            
window = Tk()

bike = ["BMW","Hayabhusa","Ducati"]

x = IntVar()
# variable = links all the radio buttons together through a common control variable — in this case, x.
# .pack = .pack() makes the widget visible and decides its position automatically.
for i in range(len(bike)):
    radio_button = Radiobutton(window,text=bike[i],variable=x,value=i,
                               font=("impact",30,"bold"),padx=50,pady=10,command=Print)
    
    radio_button.pack(anchor=W)


window.mainloop() 