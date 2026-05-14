num = int(input("enter the number"))

if num>1:
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            print(f"{num} is not prime number because prime number divides only 1 and itself but {num} divided by{i}")
            break
    else:
        print(f"{num} is prime number")

else:
    print(f"worng input")