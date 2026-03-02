# class Bank_account:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print("Your account balance is : ",self.balance)
#     def withwarl(self,amount):
#         self.balance -= amount
#         if (self.balance >= amount):
#             print("Withwarl success.. ")
#         else:
#             print("Not enough balance")
#     def showbalance(self):
#         print("Your account balance is :",self.balance)
# a1 = Bank_account("Saurav",1000)
# a2 = Bank_account("Priyam",1000)
# a1.deposit(500)
# a1.withwarl(500)
# a1.showbalance()

# -----------------------------------------------------------------------
# class Students:
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print("Your Name is ",self.name,"and your marks is",self.marks)
#     def is_pass(self,marks):
#         if(marks>= 40):
#             print("Pass")
#         else:
#             print("Fail")
# s1 = Students("Saurav",90)
# s1.display()
# s1.is_pass(85)

# ----------------------------------------------------------------------------
# class Product:
#     def __init__(self,name, price):
#         self.name = name
#         self.price = price
#     def show(self):
#         print("Product:",self.name,"Price:",self.price)
# p1 = Product("Apple",50)
# p2 = Product("Mango",40)
# p3 = Product("Guava",60)
# p4 = Product("Litch",65)
# p2.show()
# p1.show()
# p3.show()
# p4.show()

# -----------------------------------------------------------------------------
# class Employee:
#     def __init__(self,name, salary):
#         self.name = name 
#         self.salary = salary
#     def increase_salary(self,amount):
#         self.salary += amount
#     def show(self):
#         print(self.name," After increase amount:",self.salary)
# e1 = Employee("Saurav",50000)
# e1.increase_salary(500)
# e1.show()
        
# -----------------------------------------------------------------------------
# class Book:
#     def __init__(self,title,author,available):
#         self.title = title
#         self.author = author
#         self.available = available
#     def borrow_book(self):
#         if (self.available >= 0):
#             print("aviable",self.available)
#         print("Not aviable")
#     def return_book(self):
#         print(True)
#     def status(self):
#         print(self.author,self.title,self.available)
# b1 = Book("Dragons","Saurav",10)
# b1.borrow_book()
# b1.status()
