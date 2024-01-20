#1
from w3schools.classes import Person

class Student(Person):
    def __init__(self, name):
        self.name = name
    
#2
class Person:
    def __init__(self, fname):
        self.firstname = fname  

    def printname(self):
        print(self.firstname)

class Student(Person):
    pass

x = Student("Mike")
x.printname()