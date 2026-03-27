# Lavel 1
# program 1
# for i in range(1,11):
#     print(i)

# program 2
# for i in range(11,1,-1):
#     print(i)

# program 3
# for i in range(1,51):
#     if i %2== 0:
#         print(i)

# program 4
# for i in range(1,51):
#     if i %2 != 0:
#         print(i)

# program 5
# n = int(input("enter a number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# program 6
# n = int(input("enter a number: "))
# for i in range(1,n+1):
#     print(i)

# program 7
# n = int(input("enter a number:  "))
# for i in range(n, 0, -1):
#     print(i)

# program  8
# sum = 0
# for i in range(1,101):
#     sum = sum +i
#     print(sum)

# # program 9
# for i in range(1,11):
#     print(i,end=" ")

# program 10
# for i in range(1,11):
#     print(i*i)

# Lavel 2
# program 1
# n = int(input(("enter a number: ")))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# program 2
# n = int(input("enter a number:  "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# program 3
# n = int(input("enter a number:.."))
# count = 0
# while n>0:
#     n//=10
#     count +=1
# print(count)


 
# program 4
# n = int(input("enter a number "))
# rev = 0
# while n > 0:
#     digit = n% 10
#     rev = rev *10 + digit
#     n //= 10
# print(rev)


# program 15
# n = int(input("enter a number: "))
# temp = n
# rev = 0
# while n> 0:
#     digit = n%10
#     rev = rev *10 + digit
#     n//= 10
# if temp == rev:
#     print("palindrome")
# else:
#     print("not palinodrom")

# program 16
# n = int(input("Enter number: "))
# sum = 0
# while n > 0:
#     sum += n % 10
#     n //= 10
# print(sum)

# program 17
# n = int(input("Enter number: "))
# flag = True

# for i in range(2, n):
#     if n % i == 0:
#         flag = False
#         break

# if flag and n > 1:
#     print("Prime")
# else:
#     print("Not Prime")

# program 18
# for n in range(2, 101):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#             break
#     if prime:
#         print(n)

# program 19
# n = int(input("Enter number: "))
# max_digit = 0

# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n //= 10

# print(max_digit)

# # program 20
# n = int(input("Enter number: "))
# min_digit = 9

# while n > 0:
#     digit = n % 10
#     if digit < min_digit:
#         min_digit = digit
#     n //= 10

# print(min_digit)

# program 21
# for i in range(1, 5):
#     print("*" * i)

# program 22
# for i in range(4, 0, -1):
#     print("*" * i)

# program 23
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# program 24
# for i in range(1, 5):
#     print(str(i) * i)

# program 25
# for i in range(1, 4):
#     print("*" * (2*i - 1))

# program 26
# for i in range(4):
#     print("*" * 4)

# program 27
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end="")
#     print()

# program 28
# for i in range(1, 5):
#     print(" "*(4-i) + "*"*(2*i-1))

# program 29
# for i in range(4, 0, -1):
#     print(" "*(4-i) + "*"*(2*i-1))

# program 30
# num = 1
# for i in range(1, 5):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# program 31
# n = int(input("Enter number: "))
# temp = n
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum += digit ** 3
#     n //= 10

# print("Armstrong" if sum == temp else "Not Armstrong")

# program 32
for n in range(1, 1001):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == n:
        print(n)

# program 33
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b

# program 34
a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(gcd)

# program 35
a = int(input("Enter a: "))
b = int(input("Enter b: "))
lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print(lcm)

# program 36
n = int(input("Enter decimal: "))
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print(binary)

# program 37
binary = input("Enter binary: ")
decimal = 0
power = 0

for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print(decimal)

# program 38
n = int(input("Enter number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

print("Perfect" if sum == n else "Not Perfect")

# program 39
import math

n = int(input("Enter number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum += math.factorial(digit)
    n //= 10

print("Strong" if sum == temp else "Not Strong")

# program 40
s = input("Enter string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print(count)

# program 41
base = int(input("Base: "))
exp = int(input("Exponent: "))
result = 1

for i in range(exp):
    result *= base

print(result)

# program 42

s = input("Enter string: ")
rev = ""

for ch in s:
    rev = ch + rev

print(rev)

# program 43
s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# program 44
s = input("Enter string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# program 45
