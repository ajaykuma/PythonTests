#Inheritance
'''
Docstring for Example3.main
Allows a class to inherit attributes and methods from another class
Helps with code reusability & extensibility
Eample: class Child(Parent)
        class Sub(Super)
'''

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    

class Dog(Animal):
    #unique methods only for Dogs
    def speak(self):
        print("Woof!")

class Cat(Animal):
    #unique methods for Cats
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    #pass
    #unique methods for Mice
    def speak(self):
        print("Squeek!")
