num=int(input("enter the number="))

temp=num
digits=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**digits
    temp=temp//10
    
if sum==num:
    print(f"{num} is Amstrong Number")
    
else:
    print(f"{num} is Not Amstrong Number")