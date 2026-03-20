# class Inventory:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# I1 = Inventory("Saurav",5000)
# print(I1.name,I1.price)

def sorting():
    name = input("Enter Your name")
    v_count = 0
    c_count = 0
    for i in name:
        if (i == "a" or "e" or "i" or "o" or "u"):
          v_count = v_count +1
        else:
            c_count = c_count +1
    print("vowel",v_count,"Counsant",c_count)
sorting()    

        