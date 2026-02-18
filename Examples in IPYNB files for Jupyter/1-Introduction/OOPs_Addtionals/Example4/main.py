#Multiple and multi-level in heritance
'''
Docstring for Example4.main
multiple inheritance = inherit from more than one parent class
                       C(A,B)

multilevel inheritance = inherit from parent which inherits from another parent
                         C(B) <- B(A) <- A
'''
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")
    
    def sleep(self):
        print(f"This {self.name} is sleeping")

#Parent1
class Prey(Animal):
    #pass
    def flee(self):
        print(f"This {self.name} is fleeing")

#Parent2
class Predator(Animal):
    #pass
    def hunt(self):
        print(f"This {self.name} is hunting")

#Child1
class Rabbit(Prey):
    pass

#Child2
class Hawk(Predator):
    pass

#Child3
class Fish(Prey,Predator):
    pass

