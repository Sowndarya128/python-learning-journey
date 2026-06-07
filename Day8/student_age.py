class Student:
    def __init__(self,age):
        self.age = age
    def display(self):
        print("Age: ",self.age)
s1 = Student("22")
s1.display()