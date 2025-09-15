def check_number(num):
    if num == 0:
        return "Zero"
    parity = "Even" if num % 2 == 0 else "Odd"
    sign = "Positive" if num > 0 else "Negative"
    return f"{sign} {parity}"
print(check_number(10))
print(check_number(-5))
print(check_number(0))