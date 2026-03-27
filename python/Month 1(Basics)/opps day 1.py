# Classes and objects:
# class dragons:
#     print("Saurav and Priyam")
# saurav = dragons()
# print(saurav)
# # dragons()

# ---------------------------------------
# class Student:
#     def __init__(self, name, age,city):
#         self.name = name
#         self.age = age
#         self.city = city

# s1 = Student("Saurav", 21,"indore")
# priyam = Student("Priyam",20,"chennai")
# print(s1.name)
# print(s1.age)
# print(s1.city)
# print(priyam.name)
# print(priyam.age)
# print(priyam.city)

# ---------------------------------------
# class car:
#     def __init__(saurav,name,brand,color):
#         saurav.name = name
#         saurav.brand = brand
#         saurav.color = color
# s1 = car("farari","yehama","black")
# s2 = car("lamboroni","abc","blue")
# print(s2.name)
# print(s2.brand)
# print(s2.color)

# -------------------------------------

# Practice Task 1: Person
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s = Person("Saurav",20)
# p = Person("Priyam",35)
# print(s.name)
# print(s.age)
# print(p.name)
# print(p.age)

# ---------------------------------------
# | Practice Task 2: Book
class Book:
    def __init__(book,title,author,price):
        book.title = title
        book.author = author
        book.price = price
ssp = Book("The legend of Dragons","Priyam and Saurav",999)
print(ssp.title)
print(ssp.author)
print(ssp.price)        