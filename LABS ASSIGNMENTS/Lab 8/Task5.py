from datetime import datetime

def validate_and_format_date(date_str):
    """
    Validates and formats a date string.
    - The input date string should be in the format 'DD-MM-YYYY'.
    - If valid, returns the date in the format 'YYYY-MM-DD'.
    - If invalid, raises a ValueError.
    """
    try:
        # Parse the date string
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        # Return the formatted date
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected 'DD-MM-YYYY'.")

# Test cases
assert validate_and_format_date("08-09-2025") == "2025-09-08", "Test case 1 failed"  # Valid date
assert validate_and_format_date("01-01-2000") == "2000-01-01", "Test case 2 failed"  # Valid date
assert validate_and_format_date("31-12-1999") == "1999-12-31", "Test case 3 failed"  # Valid date

# Test case 4: Invalid date format
try:
    validate_and_format_date("2025-09-08")
except ValueError:
    pass
else:
    assert False, "Test case 4 failed"

# Test case 5: Invalid day or month
try:
    validate_and_format_date("32-13-2025")
except ValueError:
    pass
else:
    assert False, "Test case 5 failed"

print("All test cases passed!")