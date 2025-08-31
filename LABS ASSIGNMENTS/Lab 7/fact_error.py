
def fact(n):
    if n == 0 or n == 1:  # Base case for factorial
        return 1
    else:
        return n * fact(n - 1)  # Correct recursive call

print(fact(5))