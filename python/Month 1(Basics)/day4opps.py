# class BankAccount:
#         def __init__ (self ,balance) :
#             self.balance = balance
# acc = BankAccount (1000)    
# acc.balance = 1000000 #A Unsafe
# print(acc.balance)

# # ---------------------------------------------
# class BankAccount:
#     def __init__(self,balance):
#         self._balance = balance


# _balance signals protected status

# ----------------------------------------------
class BankAccount:
    def __init__ (self, balance):
        self.__balance = balance
acc = BankAccount (1000)
print(acc.__balance) #X ERROR

# -----------------------------------------------
# class BankAccount:
#     def __init__ (self, balance):
#         self.__balance = balance
#     def deposit (self, amount):
#         self.__balance += amount
#     def show_balance (self):
#         print("Balance:", self.__balance)