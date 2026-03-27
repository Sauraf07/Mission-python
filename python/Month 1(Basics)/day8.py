# Task 1
num = int(input("enter the number. "))
if num%2==0:
    print("number is even ")
elif num%2!=0:
    print("Num is odd")

# task 2
num = int(input("enter the number. "))
if num>0:
    print("number is positive ")
elif num==0:
     print("Num is zero")
elif num<0:
     print("number is negative")

# task 3
num = int(input("enter the 1st number. "))
num1 = int(input("enter the 2nd number. "))
if num>num1:
    print("1st no is grater")
elif num<num1:
    print("2nd no is grater")

# task 4
num = int(input("enter the 1st number. "))
num1 = int(input("enter the 2nd number. "))
num2 = int(input("Enter the 3rd number."))
if ((num>num1) & (num>num2)):
    print("1st no is grater")
elif ((num1>num2) & (num1>num)):
    print("2nd no is grater")
elif ((num2>num1) & (num2>num)):
    print("3rd no is gratest")

# task 5
age = int(input("enter your age"))
if age>=18:
    print("you can vote")
else:print("you cannot vote")

# task 6
mark = int(input("enter marks "))
if mark>=90:
    print("you get A")
elif mark<=89 and mark>=75:
    print("you get B grade")
elif mark<=74 and mark>=50:
    print("you get C grade")
elif mark <50:
    print("you fail")

# task 7
num1 = int(input("enter the 1st no. "))
num2 = int(input("enter the 2nd number"))
operator = input("enter the operation like (+,-,*,/)")

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Invalid operator")

# task  8
year = int(input("enter the year "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Year is leap yr")
else:
    print("not leap yr")

# task 9
num = int(input("enter 1st no. "))
if (num)/3:
    print("no. is divisible by 3")
elif num/5:
    print("no is divisible by 5")
else:
    print("no. is not divisible by both ")

# task 10


