# An abstract class is like a blueprint for other classes.
# You cannot create an object of an abstract class directly.
# It is used to force child classes to implement certain methods.

# Abstract Class :- A class which contain one or more abstract method
# Abstract Method :- A Method that has a declaration but not implementation

# Use of abstract class :-
# Preventing Instantiation of Incomplete Classes: You cannot directly instantiate an abstract class that 
# has abstract methods. This prevents the creation of objects that lack the necessary functionality, 
# ensuring that only fully implemented (concrete) classes can be used.

from abc import ABC , abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Square(shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side