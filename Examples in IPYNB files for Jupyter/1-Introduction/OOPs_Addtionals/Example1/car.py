from main import Car
car1 = Car("Mustang",2025,"red",False)
car2 = Car("Corvett",2021,"blue",True)

print(car1)
print(car1.for_sale,car1.model,car1.year)
print(car2.for_sale,car2.model,car2.year)

car1.drive()
car2.stop()

car1.drive2()
car2.stop2()

car1.drive3()
car2.stop3()

car1.describe()
