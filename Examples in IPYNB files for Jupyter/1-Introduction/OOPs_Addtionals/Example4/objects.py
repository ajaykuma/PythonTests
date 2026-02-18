from main import Prey, Predator, Rabbit, Fish, Hawk
'''
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
#rabbit.hunt() #Cant hunt

#hawk.flee() #Cant flee
hawk.hunt()

fish.flee()
fish.hunt()

print("Usages when multilevel inheritance")
rabbit.eat()
hawk.eat()
fish.eat()

rabbit.sleep()
hawk.sleep()
fish.sleep()
'''
rabbit = Rabbit("Bug")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
hawk.sleep()
fish.eat()
