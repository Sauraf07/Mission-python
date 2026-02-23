Name = input("Enter Your Name : ")
s1= int(input("Enter The marks of English: "))
s2= int(input("Enter The marks of Hindi: "))
s3= int(input("Enter The marks of Science: "))
s4= int(input("Enter The marks of Social Science: "))
s5= int(input("Enter The marks of Maths: "))

Total_marks = s1+s2+s3+s4+s5
percantage = ((s1+s2+s3+s4+s5)/5)
def calculation():
    if percantage >= 90 :
        print("Total Percantage ",percantage,"You Got A Grade.")
    elif percantage >= 75:
        print("Total Percantage ",percantage,"You Got B Grade.")
    elif percantage >= 60:
        print("Total Percantage ",percantage,"You Got C Grade.")
    elif percantage >= 45:
        print("Total Percantage ",percantage,"You Got D Grade.")
    else:
        print("Total Percantage ",percantage,"You Fail.")

print(Name)
print("----------------------------------------------------")
print("Marks in English: ",s1)
print("Marks in Hindi: ",s2)
print("Marks in Science: ",s3)
print("Marks in Social Science: ",s4)
print("Marks in Maths: ",s5)
print("----------------------------------------------------")
print("Total Marks: ",Total_marks)
print("Percantage: ",percantage,("%"))
calculation()