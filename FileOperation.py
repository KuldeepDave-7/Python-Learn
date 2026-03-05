# Fil Detection

import os

file = "C:\\Users\\kulde\\OneDrive\\Desktop\\hello.txt.txt"

if os.path.exists(file):
    print("This file exists :) ")
    if os.path.isfile(file):                  # Check if its file
        print("This is a file ")            
    elif os.path.isdir(file):                 # Check if its folder
        print("This is a folder ")    

else:
    print("Sorry :( this file does not exist")
    
# Read a file

with open("C:\\Users\\kulde\\OneDrive\\Desktop\\Hello.txt") as file:
    print(file.read()) 

# Write file 

Text = "Hello Whats Up \n My name is kuldeep \n i am very nonchalant and my heigh is 6'4 \n"
with open('text.txt','w') as file :          # 'w' for write if we use 'a' append we can add more to the existing
    file.write(Text)   

# copyfile() : Copies content of a file
# copy()     : Copies content + permission + destination can be directory
# copy2()    : copy() + copies metadata

import shutil

shutil.copyfile('text.txt','C:\\Users\\kulde\\OneDrive\\Desktop\\copy.txt')  # source, destination

# Move file and folder

import os

source = "text.txt"
destination = "C:\\Users\\kulde\\OneDrive\\new.txt"

try :
    if os.path.exists(destination):
        print("Their is a file already there")
    else:
        os.replace(source,destination)   
        print("File Moved")

except FileNotFoundError:
    print("FILE NOT FOUND")

# Delete file and folder and folder which contain file

import os
import shutil

path = 'folder'
try:
    #os.remove(path)             # Deletes file
    #os.rmdir(path)               # Deletes Empty folder or directory
    shutil.rmtree(path)            # Deltes folder with file
except FileNotFoundError:
    print("File not found")

# Modules :- A file containing python code. May contain functions, classes etc. Used in modular programming To seprate program into parts  
# This is our main module 

#import practise              # Through this way we can access functions from different modules
#import practise as new       # Another Way of importing module in which you can give it custom name
#from practise import hello   # Another way of importing
#from practise import *       # Import all

#practise.hello()

# help("modules") List all modules