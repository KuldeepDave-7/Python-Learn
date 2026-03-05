from tkinter import*

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def move_left(event):    
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

window = Tk()
window.geometry("420x420")

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)

label = Label(window,width=10,height=5,bg="light pink")
label.pack()

window.mainloop()

# With canvas :-


window = Tk()

def move_up(event):
     canvas.move(myPhoto,0,-10)  # Coordinates of image for UP
def move_left(event):    
     canvas.move(myPhoto,-10,0)

window.bind("<w>",move_up)
window.bind("<a>",move_left)

canvas = Canvas(window,width=200,height=100)
canvas.pack()

photo = PhotoImage(file="")
myPhoto = canvas.create_image(0,0,image=photo,anchor=NW)  # Coordinate of where to place the image with anchor 

window.mainloop()