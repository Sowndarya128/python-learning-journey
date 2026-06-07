class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name:",self.name)

s1 = Student("Sowndarya")
s1.display()