# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def deposit(self,amount):
#         self.__balance += amount
#     def withdraw(self,amount):
#         self.__balance -= amount
#     def show(self):
#         print(self.__balance)
        
# a1 = BankAccount(1000)
# a1.show()

# ---------------------------------------------------------
# class Student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def set_marks(self,marks):
#         self.__marks = marks
#     def get_marks(self):
#         print(self.__marks)
# s1 = Student(45)
# s1.get_marks()

# ------------------------------------------------------------
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary  = salary
#     def Increase_salary(self,amount):
#         self.__salary += amount
#     def get_salary(self):
#         print(self.name,self.__salary)
# e1 = Employee("Saurav",15000)
# e1.get_salary()

# ----------------------------------------------------------------
# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
#     def Set_password(self,new_password):
#         self.__password = new_password
#     def check_password(self,password):
#         if self.__password == password:
#             print("Correct")
#         else:
#             print("Wrong")
# u1 = User("Saurav",1)
# u1.Set_password(456)
# u1.check_password(4564)

# --------------------------------------------------------------
# class Rectangle:
#     def __init__(self,length,width):
#         self.__length = length
#         self.__width = width
#     def area(self):
#         print("Area:",self.__length * self.__width)
#     def perimeter(self):
#         print("Perimeter: ", self.__width + self.__length)
# r1 = Rectangle(5,3)
# r1.area()
# r1.perimeter()
        