import random
from tkinter import *

def next_turn(row,col):
    global player

    if Mesh[row][col]['text'] == "" and check_winner() is False:
        
        if player == players[0]:
            Mesh[row][col]['text'] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text=player+" Turn")
            elif check_winner() is True:
                label.config(text=players[0]+" Won")
            elif check_winner() == "Tie":
                label.config(text="Tie !")  

        else:
            Mesh[row][col]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=player+" Turn")
            elif check_winner() is True:
                label.config(text=players[1]+" Won")
            elif check_winner() == "Tie":
                label.config(text="Tie")               

def check_winner():
    for row in range(3):
        if Mesh[row][0]['text'] == Mesh[row][1]['text'] == Mesh[row][2]['text'] != "":
            return True
        elif Mesh[0][row]['text'] == Mesh[1][row]['text'] == Mesh[2][row]['text'] != "":
            return True

    if Mesh[0][0]['text'] == Mesh[1][1]['text'] == Mesh[2][2]['text'] != "":
        return True

    elif Mesh[0][2]['text'] == Mesh[1][1]['text'] == Mesh[2][0]['text'] != "":
        return True
    
    elif empty_space() is False:
        return "Tie"
    
    else:
        return False
    
def empty_space():
    space = 9

    for row in range(3):
        for col in range(3):
            if Mesh[row][col]['text'] != "":
                space -=1

    if space == 0:
        return False
    else:
        return True
                  
window = Tk()

players = ["X","O"]
player = random.choice(players)

label = Label(window,text=player+" Turn",font=("Consolas",30,"bold"))
label.pack()

Mesh = [[0,0,0],
        [0,0,0],
        [0,0,0]]

frame = Frame(window)
frame.pack()

for i in range(3):
    for x in range(3):
        Mesh[i][x] = Button(frame,text="",font=("consolas",40),width=5,height=2,command=lambda Row=i,Col=x: next_turn(Row,Col))
        Mesh[i][x].grid(row=i,column=x)
window.mainloop()