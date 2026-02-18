'''
Object = A "bundle" of attributes(variables) and methods(functions)
we always need a class to create many objects

Class = (blueprint) used to design the structure & layout of an object
'''
'''
class variables = Shared among all instances of a class
                  Defined outside the constructor
                  Allow you to share data among all objects created from that class
'''
class Car:
    def __init__(self,model, year,color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")

    def drive2(self):
        print(f"You drive the {self.model}")
    
    def stop2(self):
        print(f"You stop the {self.model}")

    def drive3(self):
        print(f"You drive the {self.color} {self.model}")
    
    def stop3(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.model} {self.color}")
