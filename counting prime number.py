a=[]
start =int(input("enter start num:"))
end = int(input("enter end num:"))

for num in range(start , end+1):
    if num>1:
        for i in range (2, int(num**0.5)+1):
            if num%i==0:
                break
        else:
            a.append(num)
            
print(len(a))