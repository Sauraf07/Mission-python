# class Animal:
#     def eat(self):
#         print("can eat")
# class Dog(Animal):
#     def bark(self):
#         print("Bark")
# a1 = Dog()
# a1.eat()
# a1.bark()

# -------------------------------------------------------------------
# class Engine:
#     def __init__(self,brand):
#             self.brand = brand
#     def start_engine(self):
#           print(self.brand,"Started....")
# class car(Engine):
#       def drive(self):
#             print("car is running")
# v1 = car("TATA")
# v1.start_engine()
# v1.drive()

# --------------------------------------------------------------------
# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#     def show_info(self):
#         print("My name is ",self.name,"and i am ",self.age)
# class student(Person):
#     def rollno(self,roll_no):
#         self.roll_no = roll_no
#         print("my roll no is.",self.roll_no)
#     def study(self):
#         print("I am studing")
# s1 = student("Saurav",20)
# s1.show_info()
# s1.study()
# s1.rollno(23)

# -----------------------------------------------------------------
# class employee:
#     def __init__(self,name, salary):
#         self.name = name 
#         self.salary = salary
#     def show_salary(self):
#         print("My name is ",self.name,"and my salary is",self.salary)
# class Manager(employee):
#     def manage_team(self,department):
#         self.department = department
#         print("I am from ",self.department,"Department")
# e1 = Manager("Saurav",50000)
# e1.show_salary()
# e1.manage_team("IT")       

# ------------------------------------------------------------------
class Rectangle:
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
        
class shape(Rectangle):
    def area(self):
        print(self.length * self.bredth)
    def perimeter(self):
        print(self.length + self.bredth)
s1 = shape(4,5)
s1.area()
s1.perimeter()
        