def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    if op in operations:
        result = operations[op](a, b)
        print("Result:", result)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()