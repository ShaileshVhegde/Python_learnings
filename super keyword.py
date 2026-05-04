class ParentClass:
    def parent_method(self):
        print("This is the parent method.")
        
class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        
    def call_parent_method(self):
        super().parent_method()  # Calling the parent method using super()
        
child_object = ChildClass()
child_object.child_method()  # Output: This is the child method.]
child_object.call_parent_method()  # Output: This is the parent method.

class Employee:
    def __init__(self, name, id):
        self.name =name
        self.id = id
        
class Programmr(Employee):
    def __init__(self, name, id, lang):
        # self.name = name
        # self.id = id
        super().__init__(name, id)
        self.lang = lang
        
rohan = Employee("Rohan", 101)
harry = Programmr("Harry", 102, "Python")

print(rohan.name)  # Output: Rohan
print(rohan.id)    # Output: 101
print(harry.name)  # Output: Harry
print(harry.id)    # Output: 102

    xxxbhh
