#in python there are no access modifiers like public, private, protected but we can achieve the same functionality using some conventions.
#using single underscore _ before a variable or method name indicates that it is intended for internal use only (protected)
#using double underscore __ before a variable or method name indicates that it is intended for internal use only and it will be name mangled (private)
#it also calls name mangling which means that the variable or method name will be changed to _ClassName__VariableName or _ClassName__MethodName
class Student:
    def __init__(self):
        self.name ="shalini"
        self._age = 20
        self.__id = 12345
        
    def _show(self):
        print(f"Name: {self.name}, Age: {self._age}, ID: {self.__id}")
        return "shailesh"
s1 = Student()
s2 = Student()
print(s1.name) #public
print(s1._age) #protected
print(s1._show()) #protected method
#print(s1.__id) #private variable will raise an error
#so we can access the private variable using name mangling affter object name we can use _ClassName__VariableName to access the private variable
print(s1._Student__id) #private variable