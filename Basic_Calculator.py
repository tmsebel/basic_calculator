# Basic Calculator Program
# We're going to add, subtract, multiply, and divide two numbers.
def calculator():
    print("Welcome to the Basic Calculator!")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print("The result is:", result)
        elif operation == '-':
            result = num1 - num2
            print(f"The result is: {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"The result is: {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()