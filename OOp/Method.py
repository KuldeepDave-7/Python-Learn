
#Method Overriding:- allows child class to provide specific execution for method that is already def in parent clas

class Janwar:
    def eat(self):
        print("Animal is eating")

class rabbit(Janwar):
    def eat(self):
        print("This rabbit is eating his food")     # Method Overriding

Rabbit = rabbit()

Rabbit.eat()

# Method chaining

class car:
    def start(self):
        print("Start the car")
        return self

    def increase(self):
        print("Increase the speed of car")
        return self

    def brake(self):
        print("Applying brakes to the car")
        return self

    def stop(self):
        print("Stop the car")
        return self

Car = car()

Car.start().increase().brake().stop()