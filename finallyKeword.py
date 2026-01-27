def func():
    try:
        i=[1,2,3,4]
        index=int(input("Enter an index: "))
        print(f"Element at index {index} is {i[index]}")
        return 1
    except :
        print("An error occurred.")
        return 0
    finally:
        print("Execution of the try-except block is complete.")
    # print("This line is outside the try-except-finally block.")
result = func()
print(result)