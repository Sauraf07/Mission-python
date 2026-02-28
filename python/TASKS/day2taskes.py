# task 1

# class product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
# first = product("Milk", 40, 5)
# second = product("Banana", 50, 10)
# firstprice = first.price * first.quantity
# secondprice = second.price * second.quantity
# total = firstprice + secondprice
# print(total)
# print(firstprice)
# print(secondprice)

# # print(first.name)
# # print(first.price)
# # print(first.quantity)
# # print("----------------------------")
# # print(second.name)
# # print(second.price)
# # print(second.quantity)
# # print("Your Bill" )

# task 2
# class Employee:
#     def __init__(self,name,id,salary):
#         self.name = name
#         self.id = id
#         self.salary = salary
# p1 = Employee("Saurav",21,50000)
# p2 = Employee("E2",1,12)
# p3 = Employee("E3",2,22)
# print(p1.name)
# print(p1.id)
# print(p1.salary)
# print(p2.name)
# print(p2.id)
# print(p2.salary)
# print(p3.name)
# print(p3.id)
# print(p3.salary)

# task 3
# class Person:
#     def __init__(self,name,age,city):
#         self.name = name
#         self.age = age
#         self.city = city
# p1 = Person("Saurav",20,"indore")
# print("Hi, I am ",p1.name,"I am ",p1.age,"years old and i live in ",p1.city)

# task 4
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
# o1 = Rectangle(5,6)
# print("Area: ",o1.length * o1.width)

# task 5
# class Mobile:
#     def __init__(self,brand, model, price):
#         self.bd = brand
#         self.md = model
#         self.pr = price
# m1 = Mobile("Apple","16x",1000000)
# m2 = Mobile("Apple","14x",1000000)
# m3 = Mobile("Apple","13x",1000000)

# print(m1.bd,m1.md,m1.pr)
# print(m2.bd,m2.md,m2.pr)
# print(m3.bd,m3.md,m3.pr)




class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
first = product("Milk", 40, 5)
second = product("Banana", 50, 10)
print(first.name)
print(first.price)
print(first.quantity)
print("----------------------------")
print(second.name)
print(second.price)
print(second.quantity)
bill1 = (first.price * first.quantity)
bill2 = (second.price * second.quantity)
print("Your First bill is ",bill1)
print("Your Secound bill is ",bill2)
finalbill = bill1 + bill2
print("And your total bill is ",finalbill)