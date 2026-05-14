num=int(input("entre the number"))
print("count od num=",len(str(abs(num))))


temp=num
count=0
while temp>0:
    count+=1
    temp=temp//10
    
print(f"count={count}")