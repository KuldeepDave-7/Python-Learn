# User Input 
name = input("What is your name: ")
print(name)

age = int(input("what is your age: "))
print(name +" age is: "+ str(age)) 

# Math Function
import math 

pi = 3.14
x = 4
y = 6

print(round(pi))
print(math.ceil(pi)) # Round off to the nearest number 
print(math.floor(pi))
print(abs(pi)) # This will tell you how far the number is from zero
print(pow(pi,2))
print(math.sqrt(400))
print(max(x,y))

# Using If Else statement :- A Block Code that will execute if it's condition is true

age = int(input("How Old Are Your : "))

if age == 15:
    print("You are under age :D")

elif age >= 50:
   print("You are above age")

elif age <= 0:
   print("You are not born yet")   
else :   
  print("Your are adult ")
  
# Logical Operaters :- Used to check If two or more condition statement (and, or, not)

temp = int(input("What is the temperature today"))

if temp >=0 and temp <=30 :  # In (and) operater both the condition must be true
    print("Temperature is normal to go outside")

elif temp < 0 or temp > 30 :  # In (or) operatore one of the condition must be true 
    print("Temperature is not normal today! ") 

# using not operator we can flip the statement if its true then it will be flip to false
  
if  not(temp >=0 and temp <=30) :  # In (not) it will behave the opposite || not true -> false
  print("Temperature is normal ")  #                                         not flase -> true  

elif not(temp < 0 or temp > 30) :   
  print("Temperature is not normal today! ") 

# *args :- parameter that will pack all arguments into a tuple

def add(*args):
   sum = 0
   for i in args:
      sum = sum + i

   return sum

ans  = add(1,2,3,4,5)
print(ans)          

# **kwargs :- parameter that will pack all arguments into a dictionary 

def hello(**kwargs):
   print(kwargs['first']+ " "+kwargs['last'])

hello(first="Kuldeep",last="Dave")   

import random

x = random.randint(1,10)
y = random.random()

print(x)
print(y)

mylist = ["pen","paper","pencil","eraser"]
cards = [1,2,3,4,5,6,7,8,9,"jack","spade","ace","king","queen"]

x = random.choice(mylist)
random.shuffle(cards)

print(x)
print(cards)

# Exception :- Events detected during execution that interrupts normal flow of program

try:
    x = int(input("Enter number to divide "))
    y = int(input("Enter number to divide by "))
    ans = x/y

except ZeroDivisionError as k :                 # For specific exception
    print(k)                                    # this will also print the type of exception 
    print("You cant divide by zero !!")

except ValueError as k:
    print(k)
    print("Please enter valid value")

except Exception:                         # For all type of exception
    print("something went wrong :) ")

else :
    print(ans)

finally:                             # Whether or not we catch exception this will always execute :)   
    print("YEAHHHHH :D")     

# Walrus Operator :=

foods = list()

while food := input("What food do you like: ") != "Quit":
   foods.append(food)

# if __name__ == '__main__' :-
# Meaning :-  Every Python file (module) has a built-in variable called __name__.
#             If the file is run directly (like python myfile.py), Python sets __name__ = "__main__".
#             If the file is imported into another file, then __name__ will be set to the name of the module (i.e., the filename without .py).   

# Use case :-
# First :- It allows you to control what runs automatically when the file is executed.

# Imagine two situations:

# Without if __name__ == '__main__':
# file: myscript.py

# def greet():
#     print("Hello from greet()")

# print("Running myscript...")   # runs no matter what
# greet()


# If you run it directly:- 
# ------------------------------------------------------
# OUTPUT:- 

# Running myscript...
# Hello from greet()

# ------------------------------------------------------
# If you import it in another file:

# import myscript
# Output:

# Running myscript...
# Hello from greet()


# 😬 Problem: it runs automatically, even though you just wanted to use greet().
# ----------------------------------------------------------
# 2. With if __name__ == '__main__':
# # file: myscript.py

# def greet():
#     print("Hello from greet()")

# if __name__ == '__main__':
#     print("Running myscript...")
#     greet()


# Run directly:
# -------------------------------------------------------------
# Running myscript...
# Hello from greet()
# -------------------------------------------------------------
# Import in another file:

# import myscript


# → Nothing prints.
# ✅ You now have clean reusability — only the functions are imported, not the “demo” code.
  