from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
ITEM_SIZE = 50
BODY_PARTS = 3
class Snake:
      
      def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0,BODY_PARTS):
                  self.coordinates.append([0,0])

            for x,y in self.coordinates:
                  square = canvas.create_rectangle(x,y,x+ITEM_SIZE,y+ITEM_SIZE,fill="Red",tags="SNAKE")
                  self.squares.append(square)      

class Food :

      def __init__(self):
            x = random.randint(0,(GAME_WIDTH // ITEM_SIZE)-1) * ITEM_SIZE
            y = random.randint(0,(GAME_HEIGHT // ITEM_SIZE)-1) * ITEM_SIZE

            self.coordinate = [x,y]   

            canvas.create_oval(x,y,x+ITEM_SIZE,y+ITEM_SIZE,fill="#03fc0f",tags="FOOD")   

def Turn(snake,food):
      x,y = snake.coordinates[0]

      if direction == "Up":
            y -= ITEM_SIZE
      
      elif direction == "Down":
            y += ITEM_SIZE

      elif direction == "Left":
            x -= ITEM_SIZE

      elif direction == "Right":
            x += ITEM_SIZE
      
      snake.coordinates.insert(0,(x,y))     
      square = canvas.create_rectangle(x,y,x+ITEM_SIZE,y+ITEM_SIZE,fill="Red",tags="SNAKE",outline="white")
      snake.squares.insert(0,(square))                   

      if x == food.coordinate[0] and y == food.coordinate[1]:
           global score
           score += 1
           label.config(text="SCORE {}".format(score))
           canvas.delete("FOOD")
           food = Food()
          
           
      else:     
           del snake.coordinates[-1]

           canvas.delete(snake.squares[-1])

           del snake.squares[-1]

      if check_collison(snake) == True:
           game_over()

      else :     
         window.after(SPEED,Turn,snake,food)

def change_direction(new_direction):
      global direction

      if new_direction == 'Left':
            if direction != 'Right':
               direction = new_direction

      elif new_direction == 'Right':
            if direction != 'Left':
               direction = new_direction

      elif new_direction == 'Up':
            if direction != 'Down':
              direction = new_direction

      elif new_direction == 'Down':
            if direction != 'Up':
               direction = new_direction      

def check_collison(snake):
     x,y = snake.coordinates[0]

     if x < 0 or x >= GAME_WIDTH:
          return True
     elif y < 0 or y >= GAME_HEIGHT:
          return True
     
     for body_part in snake.coordinates[1:]:
          if x == body_part[0] and y == body_part[1]:
            return True
     
     return False

def game_over():
     canvas.delete(ALL)
     canvas.create_text((canvas.winfo_width()/2),(canvas.winfo_height()/2),text="GAME OVER",font=("consolas",55),fill="RED")

window = Tk()

window.title("SNAKE GAME")
window.resizable(False,False)

score = 0
direction = "Down"

label = Label(window,text="SCORE : {}".format(score),font=("consolas",40))
label.pack()
canvas = Canvas(window,bg="Black",height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

window.update()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = window.winfo_width()
window_height = window.winfo_height()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

window.bind("<Left>",lambda event: change_direction('Left'))
window.bind("<Right>",lambda event: change_direction('Right'))
window.bind("<Up>",lambda event: change_direction('Up'))
window.bind("<Down>",lambda event: change_direction('Down'))

snake = Snake()
food = Food()

Turn(snake,food)
window.mainloop()