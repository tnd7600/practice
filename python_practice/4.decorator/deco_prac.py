import time

def time_decorator(func):
    def wrapper(a,b):
        start_timre = time.time()
        func(a,b)
        end_time = time.time()
        print("calculated in ", end_time - start_timre)
    return wrapper


@time_decorator
def sum(a,b):
    print(f"Sum of {a} and {b} :- {a+b}")

@time_decorator
def sub(a,b):
    print(f"Subsraction of {a} and {b} :- {a-b}")

@time_decorator
def mul(a,b):
    print(f"Multiplication of {a} and {b} :- {a*b}")

@time_decorator
def div(a,b):
    print(f"Division of {a} and {b} :- {a/b}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter your choice(+ - * /): ")

if choice == "+":
    sum(num1,num2)
elif choice == "-":
    sub(num1,num2)
elif choice == "*":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        mul(num1,num2)
elif choice == "/":
    div(num1,num2)
else:
    print("Invalid choice")



