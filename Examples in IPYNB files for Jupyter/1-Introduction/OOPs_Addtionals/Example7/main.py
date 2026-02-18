#Polymorphism
'''
Docstring for Example7.main
Greek word that means to 'have many forms or faces.
An object can take many forms
1. Inheritance = An object could be treated of the same type as a parent class
2. "Duck typing" = Object must have necessary attributes/methods
'''
from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

#Since cirlce inherits from shape, it is also considered shape
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self,side,height):
        self.side = side
        self.height = height
    
    def area(self):
        return self.side * self.height * 0.5

# class Pizza:
#     def __init__(self,topping,radius):
#         self.topping = topping
#         self.radius = radius

#Using inheritance
class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping = topping
        super().__init__(radius)
        #self.radius = radius

#Creating a list of shapes
shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("pepperoni",15)]

for shape in shapes:
    print(f"{shape.area()} cm2")
