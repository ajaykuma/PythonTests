from main import Student

student1 = Student("Bob",23)
student2 = Student("tom",45)

print(student1.name)
print(student1.age)

print("Access class variable using one of the object")
print(student1.year)
print(student2.year)

#Better to access class variable using the class name where defined
print("Better to access class variable using the class name where defined")
print(Student.year)

#print(Student.__dict__)

print(Student.num_students)

#Add a new object
student3 = Student("Jammy",50)
print(Student.num_students)

print(f"my graduating class of {Student.year} has {Student.num_students}")
print(student1.name,student2.name,student3.name)

