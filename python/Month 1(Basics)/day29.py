# try:
#     result = 10/0
#     # print(result)
# except:
#     print("An Error")

try: 
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Result:", a / b)
except:
    print("Something went wrong!")