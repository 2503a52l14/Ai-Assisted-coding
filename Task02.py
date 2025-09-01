# Program to generate the multiplication table of a given number

def multiplication_table(number):
    """
    Prints the multiplication table of the given number from 1 to 10.
    """
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Input from the user
try:
    num = int(input("Enter a number to generate its multiplication table: "))
    multiplication_table(num)
except ValueError:
    print("Invalid input! Please enter a valid number.")