import random

while True:
  Choices = ["Rock","Paper","Scissors"]

  Computer = random.choice(Choices)
  Player = None

  while Player not in Choices:
     Player = input("rock,paper,scissors: ? ").capitalize()

  if Computer == Player:
     print("Tie :)")

  elif Player == "Rock":
     if Computer == "Paper":
         print("You Lose :(")
         print("Player: "+Player)
         print("Computer: "+Computer)
     else :
         print("You Win !!") 
         print("Player: "+Player)
         print("Computer: "+Computer)   

  elif Player == "Paper":
     if Computer == "Rock":
         print("You Win !!")
         print("Player: "+Player)
         print("Computer: "+Computer)
     else :
         print("You Lose :(")
         print("Player: "+Player)
         print("Computer: "+Computer)

  elif Player == "Scissors":
     if Computer == "Rock":
         print("You Lose (")
         print("Player: "+Player)
         print("Computer: "+Computer)
     else :
         print("You Win !!")
         print("Player: "+Player)
         print("Computer: "+Computer)   

  Play_again = input("DO you want to continue (Yes/No) ") 
  if Play_again == "no":
     break

print("Adioss :D ")  