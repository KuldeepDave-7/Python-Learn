# Methods of string

name = "BroCode"
print(len(name))
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o", "a"))
print(name*3)

# String Slicing :- Create a substing by exrating elements from another string
#                   indexing[] or slice()
#                   [start:stop:step] step ; 

string = "Kuldeep"

print(string[0:7])
print(string[:7])
print(string[0:])
print(string[:])
print(string[::-1]) # Reversing

# Using Slicing :-
#  
website = "https://google.com"
website2 = "https://kuldeepdave.com"

slice = slice(8,-4)

print(website[slice])
print(website2[slice]) 

# str.format() :- optional method that give user more control over displaying output

animal = "Cat"
object = "Wall"

print("The "+animal+" jumped over the "+object)
print("The {} jumped over the {}".format(animal,object))
print("The {1} jumped over the {1}".format(animal,object))            # positional argument
print("The {vehical} jumped over the {sign}".format(vehical="bike",sign="stop")) # keyword argument

text = "The {} jumped over the {}"

print(text.format(animal,object))

# Adding padding and alignmenet in string format 
name = "Bro"
print("My Name is {0}".format(name))
print("My Name is {0:15}".format(name)+"How are you")     # padding
print("My Name is {0:<15}".format(name)+"How are you")    # left align
print("My Name is {0:>14}".format(name)+" How are you")   # right align
print("My Name is {0:^15}".format(name)+"How are you")    # centre align

num = 3.1456789
num1 = 1000000
print("The number is {:.3f}".format(num))   # f for floating .3f means upto 3 decimal places
print("The number is {:,}".format(num1))    # adds comma every thousand place
