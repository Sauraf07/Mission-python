# class Car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

# c1 = Car("Tesla",800000)
# print(c1.price,c1.brand)


# ---------------------------------------------
# use of __str__() method:
# class Car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

#     def __str__(self):
#         return f"Car: {self.brand},Rs:{self.price}"
# c1 = Car("Tesla",80000)
# c2 = Car("Lamborgani",10000000)
# print(c2)
# print(c1)

# ----------------------------------------------
# use of __len__() method
class Basket:
    def __init__(self,items):
        self.items = items

    def __len__(self):
        return len(self.items)
b = Basket(["apple","mango"])
print(len(b))
        

       
        