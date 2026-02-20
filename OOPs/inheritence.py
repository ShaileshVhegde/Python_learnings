#inheritence is a feature of OOPs that allows a new class to inherit the properties and methods of an existing class. The existing class is called the parent class or base class, and the new class is called the child class or derived class.

class Employee:
    def __init__(self,name ,age):
        self.name =name
        self.age = age
        
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Manager(Employee):
    def showdetails(self):
        print(f"Manager Name: {self.name}, Manager Age: {self.age}")

e1= Employee("John", 30)
e1.show()
m1 = Manager("Alice", 40)
m1.show()
m1.showdetails()
