# Author : Code_with_Manav
# Task : Calculator

#defining the calculating functions
def sum(a, b):
    return a+b

def subtract(a, b):
    return a-b

def product(a, b):
    return a*b

def divide(a, b):
    return a/b

# Greet the user
print("Welcome to PyCalci!")

# Loop until user wants to exit
while True:

    # Ask for user input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Perform the operation based on the operator
    if operator == "+":
        result = sum(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = product(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operator == "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            continue
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Invalid operator. Please use +, -, *, /.")
        continue
    
    # Ask user if they want to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
        print("Thank you for using PyCalci!")
        break