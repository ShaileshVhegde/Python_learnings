x=[12,45,55,5]
print(dir(x))
print(help(x))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p1=Person("shailesh",19)
print(p1.__dict__)
print(help(p1))