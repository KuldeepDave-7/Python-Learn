from tkinter import *

def drag(event):
    # when an event happens (like a mouse click or key press), Tkinter automatically creates an Event object and passes it to your function.
    # event.x refers to the widget that triggered the event and is dynamically assigned at runtime.
    widget = event.widget

    widget.start_x = event.x    # Coordinate of mouse inside the box (x)
    widget.start_y = event.y    # Coordinate of mouse inside the box (y)

def drag_motion(event):
    widget = event.widget
    
    # widget.winfo_x() = Coordinate of widget relative to the window 
    # Calculating difference b/w widget postion relative to window and click point inside it.
    # Adds the mouse’s current local coordinate to that offset to find the new window coordinate.

    offset_x = widget.winfo_x() - widget.start_x      
    offset_y = widget.winfo_y() - widget.start_y
    x = event.x + offset_x
    y = event.y + offset_y

    widget.place(x=x,y=y)

window = Tk()

label1 = Label(window,bg="light pink",width=10,height=5)
label1.place(x=0,y=0)

label1.bind("<Button-1>",drag)
label1.bind("<B1-Motion>",drag_motion)

window.mainloop()