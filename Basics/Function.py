# # Functions :-It is used for specific purpose and is executed only when invoked(called)

# def hello(name, age):
#     print("HELLO BRO "+"your age is "+str(age))

# hello("kuldeep",20)    

# # Return Statement :- Fucntion send pvalu/object back to the caller
# #                     These objects are known as function return value

# def Adittion(no1,no2):
#     ans = no1+no2
#     return ans

# ans = Adittion(5,5)
# print("The answer is :"+str(ans))

# # Keyword arguments :- Arguments preceded by an identifier when we pass them order doesnt matter

# def Name(middle,first,last):
#     print("Hello "+first +middle +last )

# Name(middle="King",last="Dave",first="Kuldeep")

# # Nested Function :- Function calls inside another function calls
# #                    the inner one is resolved first
# #                    returned value is used as an argument for the next outer function 


# print(round(abs(float(int(input("Enter a positive number"))))))

# # Higher Order function:- Function that either:- a) Accepts function as a argument 
# #                                                b) Returns a function (In python function are also treated as object)

# def loud(text):
#    return text.upper()

# def quiet(text):
#    return text.lower()

# def hello(func):                           # Accept (Function) as argument
#    text = func("hello")
#    print(text)

# hello(loud)
# hello(quiet)  

# # Returns a function:-

# def divisor(x):
    
#     def dividend(y):
#         return y/x
    
#     return dividend     # Returns Memory address of dividend

# divide = divisor(2)    # Storing memory address od dividend
# print(divide(10))      # Calling dividend function through its address stored

# # Lambda Function:- Function written in 1 line using lambda keyword
# #                   Accepts any number of argument but only has 1 expression
# #                   Think of it as a shortcut (useful for short period of time, throw - away)

# # lambda parameters:expression   (syntax)

# double = lambda x : x*2
# multiply = lambda x,y : x*y
# full_name = lambda firstName, lastName : firstName + " " + lastName
# age_check = lambda x : x >= 18 if True else False # lambda x : True if x >= 18 else False 

# print(age_check(17))

# map() :- applies a function to each item in the iterable
# map(function, iterable)

shop = [("shirt",20),   # Prices in dollar
        ("pants",35),
        ("shoes",90),
        ("socks",10)]

#to_rupees = map(lambda data : (data[0],data[1]*85),shop)
to_rupees = lambda data : (data[0],data[1]*85)             # This will cast a new map object
in_rupees = list(map(to_rupees,shop))                      # map object to list

# Filter ():- Creates a collection of elements from a iterable for which a function return True
# filter (function,iterable)

friends = [("Rachel",20),
           ("Kuldeep",19),
           ("Monica",15),
           ("Davis",14)]

age = lambda data : data[1] >= 18

eligble = list((filter(age,friends)))

for i in eligble:
    print(i)

# reduce() = apply function to an iterable and reduce it to a single cumulative value.
#            perfroms func on first two element and repeat until 1 value remains 
# reduce(function,iterable)

import functools

word = ["K","U","L","D","E","E","P"]
combine = functools.reduce(lambda x,y: x+y, word)
print(combine)

digits = [5,4,3,2,1]
factorial = functools.reduce(lambda x,y : x*y,digits)
print(factorial)

