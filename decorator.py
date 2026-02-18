#Decorator function that adds behavior before and after the execution of the original function
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        func(*args, **kwargs)
        print("After function execution")
    return wrapper

#Example usage of the decorator

def say_hello(name):
    print(f"Hello, {name}!")
  

#Applying the decorator to the function

decorator(say_hello)("Bob")
