#Super()
'''
Docstring for Example6.main
Function used in a child class to call methods from a parent class.(superclass)
Allows you to extend the functionality of the inherited methods.

'''
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if {self.filled} else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,filled,radius):
        # self.color = color
        # self.filled = filled
        super().__init__(color,filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14*self.radius*self.radius} cms squared")
        #extending functionality
        super().describe()

class Square(Shape):
    def __init__(self,color,filled,width):
        # self.color = color
        # self.filled = filled
        super().__init__(color,filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,color,filled,width, height):
        # self.color = color
        # self.filled = filled
        Shape.__init__(color,filled)
        #super().__init__(color,filled)
        self.width = width
        self.height = height

circle = Circle(color = "red", filled = True, radius = 5)

print(circle.color)
print(circle.filled)
print(circle.radius)

square = Square(color = "red", filled = True, width = 5)

print(square.color)
print(square.filled)
print(square.width)
print(f"{square.width} cms")

circle.describe()



