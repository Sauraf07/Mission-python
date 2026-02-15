# Scenario 1: User Login Validation
# def login():
#     passw = 12345
#     username = 'admin'
#     name = input("entre user name: ")
#     ps = int(input("entre password: "))
#     if (ps == passw and name == username):
#         print("Login Succesfull")
#     else:
#         print("Invalid User")
# login()
    
    
   
# Scenario 2: ATM Withdrawal System
# def withdraw():
#     balance = int(input("Enter your account Balance: "))
#     min = 500
#     amount = int(input("Enter amount to widwal : "))
#     if (amount % 100 == 0):
#         balance = balance - amount
#         if(balance >= min):
#             print("widwarl succesfull")
#         else:
#             print("transection failed")
#     else:
#         print("enter a valid amount ")

# withdraw()

# Scenario 3: Student Result Processing
# def isPass():
#     marks = int(input("enter your marks: "))
#     if(marks>=40):
#         print("Pass")
#     else:
#         print("Fail")
# isPass()

# Scenario 4: Electricity Bill Calculation
# def calculateBill():
#     unit = int(input("Enter unit: "))
#     bill = 0
#     if(unit <= 100):
#         bill = unit*2
#         print(bill)
#     elif(unit>100):
#         bill = unit*3
#         print(bill)
#     elif(unit>200):
#         bill = unit*5
#         print(bill)

# calculateBill()

# Scenario 5: Online Shopping Discount
# def finalAmount():
#     bill = int(input("Enter bill amount: "))
#     if (bill>=10000):
#         bill = bill - (bill * 0.2)
#         print("Your Bill after Discount is : ",bill)
#     elif(bill>=5000):
#         bill = bill - (bill * 0.1)
#         print("Your Bill after Discount is : ",bill)
#     else:
#         print("You get no discount")
# finalAmount()