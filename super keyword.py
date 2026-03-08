class ParentClass:
    def parent_method(self):
        print("This is the parent method.")
        
class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        
    def call_parent_method(self):
        super().parent_method()  # Calling the parent method using super()
        
child_object = ChildClass()
