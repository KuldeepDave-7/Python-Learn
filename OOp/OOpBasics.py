# Python Object oriented programming :-
# Object-Oriented Programming (OOP) in Python is a programming paradigm that structures code around objects,
# which are instances of classes

# Class: A blueprint or a template for creating objects. It defines the attributes (data) and methods (functions)
#        that objects of that class will possess.

# Attributes = Characteristics of a object || Method = Action object performs 

# Object: An instance of a class. It is a concrete entity created based on the class's blueprint, 
#         holding its own set of attribute values.

class Bike:
    
    # Self :- It represent instance of class (the object itself) it represent the object itself
    # Use self. only when you want to store something inside the object
    # they become object attributes They stay alive even after the function ends
    
    wheels = 2                                        # Class variable
    
    def __init__(self,name,color,mileage,topspeed):   # init = initialize think of it as a constructor
        self.name = name                              # Attributes
        self.color = color                            # Instance Variable
        self.mileage = mileage
        self.topspeed = topspeed

    def drive(self):
        print(self.name+ " is Driving")

    def stop(self):
        print(self.name+ " is Stopped")
 
 
 
bike1 = Bike("Bmw","Black",15,200)

print(bike1.name)
print(bike1.color)
print(bike1.mileage)
print(bike1.topspeed)

bike1.drive()

# Object as argument :-

class Car :
    color = None

def change_color(vehicle,color):
     vehicle.color = color


car1 = Car()
car2 = Car()

change_color(car1,"red")   # Passing object as argument 
print(car1.color)
