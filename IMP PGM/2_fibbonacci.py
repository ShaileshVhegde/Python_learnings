num=int(input("enter the number"))

a=0
b=1

for i in range(num):

    print(a,end=" ")
    temp=a+b
    a=b
    b=temp
   
    

