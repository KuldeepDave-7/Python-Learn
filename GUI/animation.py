from tkinter import *
from ball import *
import time

# WIDTH = 500
# HEIGHT = 300

# window = Tk()

# x_speed = 7
# y_speed = 7

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# ground = PhotoImage(file='C:\\Users\\kulde\\Downloads\\Ground.png')
# main_pic = PhotoImage(file='GUI\\football.png')

# background = canvas.create_image(0,0,image=ground,anchor=NW)
# ronaldo = canvas.create_image(0,0,image=main_pic,anchor=NW)

# image_width = main_pic.width()
# image_height = main_pic.height()

# while True:
#     coordinates = canvas.coords(ronaldo)
    
#     if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
#         x_speed = -x_speed 
        
#     if(coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0):
#         y_speed = -y_speed

#     canvas.move(ronaldo,x_speed,y_speed)
#     window.update()
#     time.sleep(0.05)

# window.mainloop()

root = Tk()

WIDTH = 500
HEIGHT = 300

canvas = Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()
voll_ball = ball(canvas,0,0,100,5,5,"pink")
tenn_ball = ball(canvas,0,0,50,10,10,"light yellow")
basket_ball = ball(canvas,0,0,120,8,14,"brown")

while True:
    voll_ball.move()
    tenn_ball.move()
    basket_ball.move()
    root.update()
    time.sleep(0.05)

root.mainloop()