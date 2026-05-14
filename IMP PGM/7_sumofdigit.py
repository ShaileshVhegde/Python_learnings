num=int(input("enter the number"))

digit=0
temp=num
while temp>0:
    last_num=temp%10
    digit=last_num+digit
    temp=temp//10
    
print(f"sum of {num} is {digit}")