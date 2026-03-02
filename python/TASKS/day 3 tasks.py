# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print("Hello, my name is ",self.name,"and i am ",self.age,"years old")

# s1 = Student("Saurav",20)
# s2 = Student("Priyam",19)
# s1.introduce()
# s2.introduce()


# ----------------------------------------------------------------
# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#         print("Addition is ",self.num1 + self.num2)
#     def subtract(self):
#         print("Sub is ",self.num1 - self.num2)
#     def multiply(self):
#         print("multiply is ",self.num1 * self.num2)
# c1 = Calculator(2,5)
# c1.add()
# c1.subtract()
# c1.multiply()

# ---------------------------------------------------------------------
# class Car:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed
#     def start(self):
#         print("Car started..")
#     def accelarate(self):
#         print(self.brand,"running at " , self.speed,"KM/H")
# c1 = Car("TATA",100)
# c1.start()
# c1.accelarate()


# -----------------------------------------------------------------------
# class Bank:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def show_balance(self):
#         print("Your Balance is :",self.balance)
#     def diposit(self):
#         amount = int(input("Enter the amount to deposit: "))
#         self.balance += amount 
#         print(self.name,"Your total balance is :",self.balance)
# b1 = Bank("Saurav",500)
# b1.show_balance()
# b1.diposit()
        
# ----------------------------------------------------------------------
class Reactangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of Recatngle is ",self.length * self.width)     
    def perimeter(self):
        print("Perimeter of rectangle is :",self.length + self.width)
r1 = Reactangle(10,20)
r1.area()
r1.perimeter()   