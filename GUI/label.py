# Lable :- a Label is a widget used to display static text or images within a window.

from tkinter import *
window  = Tk()
# First argument known as the "master" specifies that the newly created label should be placed inside the GUI window
# relief :- The relief attribute can also be set to other values to achieve different visual effects

label = Label(window,text='Kuldeep',
              font=('arial',50,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED)  

label.pack()            # Places the label widget within its parent window or container. 
#label.place            # Can set custom x and y coordinates

window.mainloop()