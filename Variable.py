# A variable is a container. Behave as the value it contains

# Strings 
name = "kuldeep"
lastname = "dave"
fullname = name + " " +lastname
print("Name: " + fullname)

# char
alpha = 'a'
print (alpha)

# Integer
age = 25
age += 2
print (age)
print(type(age))

# You cant combine variables of different data types. You can do that by type casting
# wrong -> print(fullname + age)
# Right -> print(fullname + str(age))
print (fullname +" Age: " + str(age))

# Float
height =  4.5
print (height)
print ("MY height is: " + str(height))

# Boolean
Right = False
print(Right)

# Mutiple Assignment :- Allows us to assign multiple variable at the same time 

name, age, height, male = "Sushant", 20, 6.5, True
print(name)
print(age)
print(height)
print(male)