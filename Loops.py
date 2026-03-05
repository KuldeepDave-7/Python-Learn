#   While Loop :- a statement that will execute its block of code,
#                 as long as its condition remains true;

name = ""
while len(name) == 0:
   name = input("what is your name : ")

print("Hello " + name)

# Another way of writing using (not) operater  
name = None
while not name:
    name = input("Enter YOur Name: ")

print("Hello " + name)


# For Loop :- a statement that will execute its block of code limited amount of time

import time

for i in range(10,0,-1):
    print(i)
    time.sleep(1)

print("Hello New Year")

# Nested Loop:-  Inner loop will finish all of it's iteration before finishing one iteration of outer loop

row = int(input("Enter number of rows: "))
col = int(input("Enter number of col: "))

for i in range(row):
    for z in range(col):
         print("*", end=" ")
    print() 

# Loop Control statement :- Used to change the normal execution sequence of a loop

# Break :- 
while True :
     name = input("Enter Your Name: ")
     if name != "":
          break

# Continue :-
phone_num = "123-456-789"
for i in phone_num:
     if i == "-":
          continue
     print(i,end="")     

# Pass :-
for i in range(1,11):
    if i == 9:
        pass
    else:
        print(i,end=" ")