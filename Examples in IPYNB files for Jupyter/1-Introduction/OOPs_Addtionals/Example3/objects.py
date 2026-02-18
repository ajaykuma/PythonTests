from main import Dog,Cat,Mouse

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Jerry")

print(dog.name)
print(cat.name)
print(mouse.name)
print(dog.is_alive)
print(cat.is_alive)
print(mouse.is_alive)

dog.eat()
dog.sleep()
dog.speak()
cat.eat()
cat.sleep()
cat.speak()
mouse.eat()
mouse.sleep()
mouse.speak()


