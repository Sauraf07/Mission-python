# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower

#     def start(self):
#         print(f"🔧 Engine start! Power: {self.horsepower} HP")

#     def stop(self):
#         print("🔴 Engine band ho gaya!")


# # Ab Car class banao — Engine ka USE karegi
# class Car:
#     def __init__(self, brand, horsepower):
#         self.brand = brand
#         self.engine = Engine(horsepower)  # ← Engine object CAR ke andar!

#     def drive(self):
#         print(f"🚗 {self.brand} chal rahi hai!")
#         self.engine.start()  # ← Engine ka method use kar raha hai

#     def park(self):
#         print(f"🅿️ {self.brand} park ho gayi!")
#         self.engine.stop()


# # Object banao
# my_car = Car("Honda City", 120)
# my_car.drive()
# my_car.park()

# ---------------------------------------------------------------
# class Address:
#     def __init__(self, city, state, pincode):
#         self.city = city
#         self.state = state
#         self.pincode = pincode

#     def show_address(self):
#         print(f"📍 {self.city}, {self.state} - {self.pincode}")


# class Student:
#     def __init__(self, name, age, city, state, pincode):
#         self.name = name
#         self.age = age
#         self.address = Address(city, state, pincode)  # ← Address object andar!

#     def show_info(self):
#         print(f"👤 Naam: {self.name}")
#         print(f"🎂 Umar: {self.age}")
#         self.address.show_address()  # ← Address class ka method use kar raha hai


# # Object banao
# s1 = Student("Saurav", 22, "Indore", "MP", "452001")
# s1.show_info()

class Dargons:
    class Saurav:
        def __init__(self,name,role):
            self.name = name
            self.role = role
        def Show(self):
            print(self.name,self.role)
d1 = Dargons.Saurav("Saurav","1st member")
d1.Show()

# class Car:
#     class Engine:
#         def start(self):
#             print("Nested engine starts")

# car_engine = Car.Engine()
# car_engine.start()

            
        