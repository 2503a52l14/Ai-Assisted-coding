def classify_number(n):
    """
    Classifies a number as:
    - "Perfect" if the sum of its proper divisors equals the number.
    - "Abundant" if the sum of its proper divisors is greater than the number.
    - "Deficient" if the sum of its proper divisors is less than the number.
    """
    if n <= 0:
        return "Invalid"  # Only positive integers are valid

    divisor_sum = 0
    for i in range(1, n // 2 + 1):  # Loop through proper divisors
        if n % i == 0:
            divisor_sum += i

    if divisor_sum == n:
        return "Perfect"
    elif divisor_sum > n:
        return "Abundant"
    else:
        return "Deficient"

# Test cases
assert classify_number(6) == "Perfect", "Test case 1 failed"  # 6 = 1 + 2 + 3
assert classify_number(12) == "Abundant", "Test case 2 failed"  # 12 < 1 + 2 + 3 + 4 + 6
assert classify_number(8) == "Deficient", "Test case 3 failed"  # 8 > 1 + 2 + 4
assert classify_number(0) == "Invalid", "Test case 4 failed"  # Invalid input
assert classify_number(-5) == "Invalid", "Test case 5 failed"  # Invalid input

print("All test cases passed!")