# instense var vs class var means instance variable and class variable it is a variable that belongs to an instance of a class and a variable that belongs to the class itself.
class Emloyee:
    companyNmae ="Google" # class variable
    NoOfEmployee = 0 # class variable
    def __init__(self,name):
        self.name = name # instance variable
        self.raise_amount = 1.5 # instance variable
        Emloyee.NoOfEmployee += 1 # class variable
    def showDetails(self):
        print(f"Name: {self.name},  Company: {self.companyNmae}, Raise Amount: {self.raise_amount}")
    
    
emp1 = Emloyee("John")
emp1.raise_amount = 2.0 # instance variable
emp1.companyNmae = "Microsoft" # class variable

emp1.showDetails()

emp2 = Emloyee("Jane")
emp2.companyNmae = "Amazon" # class variable
emp2.showDetails()