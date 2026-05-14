num=int(input("enter the number"))
reverse_num=0
temp=num
while temp>0:
    last_digit=temp%10
    reverse_num=reverse_num*10+last_digit
    temp=temp//10

print(f"reversed number is {reverse_num}")
