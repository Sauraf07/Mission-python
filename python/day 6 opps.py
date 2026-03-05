# class Father:
#     def house(self):
#         print("Father owns a house")

# class Child(Father):
#     def bike(self,name):
#         self.name = name
#         print("Child owns a bike",self.name)

# # obj = Child()

# # obj.house()   # inherited from Father
# # obj.bike("yahama")
# F = Father()
# F.house()

# -----------------------------------------------------------
# Method Overriding
# class Animal: 
#     def speak(self): 
#         print("Animal sound") 
# class Dog(Animal):
#     def speak(self):
#         print("Bark")
# A = Dog()
# A.speak()
# When Dog().speak() is called, it outputs "Bark". The child's method takes precedence.

# ------------------------------------------------------------------
class Person:
     def greet(self):
         print("Hello") 
class Student(Person):
     pass 
s = Student() 
s.greet()