# n = int(input("Enter n: "))
# i = 1
# total = 0
# while i <= n: 
#     total = total + i
#     i = i + 1
# print("Sum:", total)

# 1(i)<=3(n)
#0(total) = t(0)+i(1) =t(1)
# 1+1=2 i=2
# 2<=3
# 1 = 1+2 =3(t)
# 2+1=3
# 3<=3
# total =3(t)+i(3) = 6(t)
# 3+1 =4
# 4<=4
# total = 6+i(4) =10
# total = 10+i(5) = 15
# total = 15+i(6)=21
# total = 21 +i(7)=28
# 1+2+3+4+5=15


# -----------------------------------------------------
num = int(input("Enter num: "))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print("Digits:", count)


