# Inheritance in OOP

class Animal:

    Alive = True

    def __init__(self): 
        pass

    def running(self):
        print(self.name+" is running")

    def sleeping(self):
        print(self.name+" is sleeping")

class Cat(Animal):
    
    def sound(self):
        print("Cat Meoww")

class Dog(Animal):

    def sound(self):
        print("Dog Bark") 


cat = Cat()
dog = Dog()

print(cat.Alive)
cat.sound()

# MULTI LEVEL INHERITANCE :- When a derived (child) class inherit another derived (child) class

class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("this animal is barking")

dog = Dog()
dog.alive
dog.eat()
dog.bark()

# super() :- super() is used to call a method from the parent class inside a child class.
#            It helps avoid repeating code that is already written in the parent class.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)

    def area(self):
       return self.length*self.width 

class cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height
    

square = square(3,3)
Cube = cube(3,3,3)

print(square.area())
print(Cube.volume())