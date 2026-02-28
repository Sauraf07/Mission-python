# class Student: 
#     def __init__(self, name): 
#         self.name = name 
#     def greet(self): 
#         print("Hello,", self.name)
# # Creating an object and calling the method 
# s1 = Student("Saurav") 
# s1.greet()
# ------------------------------------------

# class BankAccount:
#     # Use double underscores here
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def show_balance(self):
#         print("Balance:", self.balance)

# # Usage
# acc = BankAccount("Saurav", 1000)
# acc.show_balance()



# -----------------------------------------


# class BankAccount: 
#     def __init__(self, balance): 
#         self.balance = balance 

#     def deposit(self, amount):
#         self.balance += amount 
#         # This print must be indented to stay inside the function
#         print("New Balance:", self.balance)
#     def withwarl(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withwarl successful....")
#             print("Your Balance: ",self.balance)
#         else:
#             print("Not enough balance")

# # Usage
# acc = BankAccount(1000)
# acc.deposit(500)
# acc.withwarl(int(input("Enter Widwarl amount: ")))



# ---------------------------------------
class Dog: 
    def __init__(self, name): 
        self.name = name
    def bark(self): 
        print(self.name, "is barking") 
    def sleep(self): 
        print(self.name, "is sleeping") 
d1 = Dog("Tommy") 
d1.bark()
d1.sleep()