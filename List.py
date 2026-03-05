# List = Used to store multiple item in a single variable

Cars = ["audi","bmw","jeep","suzuki"]

Cars[0] = "pagani"

for i in Cars:
    print(i)

Cars.append("mercedes")   # Add item at the last on list
Cars.remove("bmw")        # Removes item in the list
Cars.pop()                # Removes last item in the list
Cars.insert(0,"omni")     # Insert at particular index
Cars.sort()
Cars.clear

# 2D list -> contain list of lists

Cars = ["audi","bmw","jeep","suzuki"]
bikes = ["ninja", "Hero", "bmw","Ducati"] 

Vehical = [Cars,bikes]

# Tuple : Collection which is ordered and unchangable meaning unlike list
#         in tuple you cant not do modification after tuple is created  

student = ("bro",21,"female")
print(student.count("bro"))
print(student.index(21))

for x in student:
    print(x)

# Set :- It is collection of unordered collection of unique elements and are mutable

another_set = {"cherry", "apple", "banana"}

list_to_set = set([1, 2, 2, 3, 4]) # Result: {1, 2, 3, 4}

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

another_set.add("kiwi")
another_set.remove("kiwi") 

empty_set = set()
# Union
print("Union :",set_a.union(set_b))

# Intersection
print("intersection :",set_a.intersection(set_b))

# Difference
print("Difference",set_a.difference(set_b))

# Dictionary:- Changable, unordered collection of unique key : value (Faster because its uses hashing)

country = {'Usa': 'Washington',
           'India': 'Delhi',
           'China': 'bejing',
           'Japan': 'tokyo'}
# country.update({'Russia': 'Moscow'})
# country.pop('china')
# country.clear()

print(country.get('India'))    # <- It provides a safer way to access dictionary elements compared to direct indexing
                               #  (e.g., dictionary[key]), as it does not raise a KeyError if the key is not found.
print(country.values())
print(country.keys())
print(country.items())

for x,y in country.items():
    print(x,y)

# Index Operator [] :- Give access to sequence element  (str,tuple,list)

name = "Kuldeep Dave"

if (name[0].isupper()):
    name = name.lower()

print(name)

first_name = name[:7]
last_name = name[8:]
last_letter = name[-1]

print(last_letter)

# List comprehension = A way to to create new list with less syntax
#                      can mimic certain lambda function, easier to read
# syntax :-            list = [expression for item in iterable]
# With condition(if)   list = [expression for item in inteable if condition]
# With both(if/else)   list = [expression if/else for item in iterable]

# Normal way :-
square = []
for i in range(1,11):
    square.append(i * i)
print(square)                     

# Using list comprehension :-

square = [i * i for i in range(1,14)]
print(square)

students = [100,90,80,70,60,50,40,30,20,10,0]

#passed = [i for i in students if i >= 30]
passed = [i if i >= 40 else "FAILED"  for i in students]
print(passed)

# Dictionary cpmprehension :- create dictionaries using an expression
#                             can replace for loops and ceratin lambda func

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if condition}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

cities_inF = {'new york':45,'delhi':60,'los angeles':70}
cities_inC = {key: round(((value-32)*(5/9))) for (key,value) in cities_inF.items()}
print(cities_inC)

# Zip(*iterable) :- aggregate elements from two or more iterable
#                   create a zip object with paired elements stored in a tuple

username = ["KULDEEP","HARRY","SHIVAM"]
password = ["p@@@assword","hello123","12344321"]

users = zip(username,password)

for i in users:
    print(i) 

for i in range(1,1000):
    print(i)    
