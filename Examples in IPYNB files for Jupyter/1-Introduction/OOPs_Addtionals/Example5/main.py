#Abstact classes
'''
Docstring for Example5.main
A class that cannot be instantiated on its own; meant to be subclassed.
we cant create objects from this class.
They can contain abstract methods, which are declared but have no implementation
and those methods are defined within children classes.
Benefits:
1. Prevents instantiation of the class itself
2. Requires children to use inherited abstract methods.
'''
from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#vehicle = Vehicle() -- will throw an error
#TypeError: Can't instantiate abstract class Vehicle with abstract methods go, stop

#class Car(Vehicle):
#    pass
##TypeError: Can't instantiate abstract class Vehicle with abstract methods go, stop

#So we need to finish defining the mthods
class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

car = Car()

car.go()
car.stop()

class MotorCycle(Vehicle):
    def go(self):
        print("You ride the bike")

    def stop(self):
        print("You ride the bike")   

motorcycle = MotorCycle()
motorcycle.go()
motorcycle.stop()

