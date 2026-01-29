questions =[
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"],
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"],
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"],
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"],
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"],
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"],
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"],
    ["What is the capital of France?","BLR","PUNE","MUMBAI","NoNE OF THE ABOVE","D"]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question of rupees {levels[i]} is: {question[0]}")
    print(f"Your options are:\n A.{question[1]}\n B.{question[2]}\n C.{question[3]}\n D.{question[4]}")

    answer=input("Enter your option (A/B/C/D): or (Q) for quit ").upper()
    if answer=="Q":
        if i==0:
            print("You have won Rs.0")
        else:
            print(f"You have won Rs.{levels[i-1]}")
        break
    elif (answer==question[-1] ):  
       print(f"Congratulations! You have won Rs.{levels[i]}")    
    else:
        print("Sorry, that's incorrect. Game over!")
        if(i<=4):
            print("Better luck next time!")
        elif(i<=9):
            print("You have won Rs.10000")
        elif(i<=14):
            print("You have won Rs.320000")
        break
print("Thank you for playing Kaun Banega Karodpati!")