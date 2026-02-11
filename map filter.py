#map
def cube(x):
    return x**3

print(cube(5))

l=[1,2,3,4,5]
newl=[]
for i in l:
    newl.append(cube(i))
print(newl)

#we can also do the above using map function
newl= list(map(cube,l))
print(newl)
#we can also use lambda function with map
newl= list(map(lambda x: x**3,l))
print(newl)

#filter
def is_even(x):
    return x%2==0

l=[1,2,3,4,5,6,7,8,9,10]
newl=[]
for i in l:
    if is_even(i):
        newl.append(i)
print(newl)
#we can also do the above using filter function
newl= list(filter(is_even,l))
print(newl)
#we can also use lambda function with filter
newl= list(filter(lambda x: x%2==0,l))
print(newl)

#reduce
from functools import reduce
def add(x,y):
    return x+y
l=[1,2,3,4,5]
print(reduce(add,l))
#we can also use lambda function with reduce
print(reduce(lambda x,y: x+y,l))
    