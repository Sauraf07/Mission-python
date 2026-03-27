class hello:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
            print("Hello", self.name)
            print("My Age is ",self.age)
s1 = hello("Saurav",20)
s1.greet()
