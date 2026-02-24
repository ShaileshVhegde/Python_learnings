#static meathod is a method that belongs to the class rather than an instance of the class. It can be called without creating an instance of the class.

class Math:
    def __init__(self,num):
        self.num = num
        
    def addtonumber(self, number):
        self.num=self.num+number
    @staticmethod
    def multiply(a,b):
        result = a * b
        return result
    

    ##
math = Math(5)
print(math.num)
math.addtonumber(10)
print(math.num)
print(Math.multiply(3,4))
