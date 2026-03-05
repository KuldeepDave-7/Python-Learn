from tkinter import *
from tkinter import messagebox

def box():
   messagebox.showinfo(title="Message Here",message="Have a good day !")
  # messagebox.showwarning(title="Warning Here",message="Closing pc in 5 sec")
  # messagebox.showerror(title="ERROR",message="Cant open settings")
  # icon :- used to change the icon = warning, question, info, error  
   if messagebox.askokcancel(title="Ask Here",message="Are you Gay") :
      print("Damm homie Gay LOL")
   else:
      print("So youre not gay")  

window = Tk()

button = Button(window,text="Click Me",command=box)
button.pack()

window.mainloop()