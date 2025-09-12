import re

def is_strong_password(password):
    """
    Validates if the given password is strong.
    A strong password:
    - Has at least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Test cases
assert is_strong_password("StrongPass1!") == True, "Test case 1 failed"
assert is_strong_password("weakpass") == False, "Test case 2 failed"
assert is_strong_password("Short1!") == False, "Test case 3 failed"
assert is_strong_password("NoSpecialChar1") == False, "Test case 4 failed"
assert is_strong_password("ValidPass123!") == True, "Test case 5 failed"

print("All test cases passed!")