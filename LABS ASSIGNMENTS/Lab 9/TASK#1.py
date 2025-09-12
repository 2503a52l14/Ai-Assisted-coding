"""
Lab 9 – Task 1
Automatic Code Commenting & Documentation
"""

# ---------------------------------------------------
# Version 1: AI-Generated Comments
# ---------------------------------------------------
def calculate_discount_ai(price, discount_rate):
    # Subtracts the discount amount (price * discount_rate / 100) from the original price
    return price - (price * discount_rate / 100)
# ---------------------------------------------------
# Version 2: Manual Comments
# ---------------------------------------------------
def calculate_discount_manual(price, discount_rate):
    # Calculate the discount amount by multiplying the price with the discount rate percentage
    # Subtract the discount amount from the original price to get the final discounted price
    return price - (price * discount_rate / 100)
# ---------------------------------------------------
# Version 3: Google-Style Docstring
# ---------------------------------------------------
def calculate_discount_google(price, discount_rate):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_rate (float): The discount rate as a percentage.

    Returns:
        float: The final price after applying the discount.
    """
    return price - (price * discount_rate / 100)
# ---------------------------------------------------
# Version 4: NumPy-Style Docstring
# ---------------------------------------------------
def calculate_discount_numpy(price, discount_rate):
    """
    Calculate the final price after applying a discount.

    Parameters
    ----------
    price : float
        The original price of the item.
    discount_rate : float
        The discount rate as a percentage.

    Returns
    -------
    float
        The final price after applying the discount.
    """
    return price - (price * discount_rate / 100)
# ---------------------------------------------------
# Version 5: New Function with Detailed Docstring
# ---------------------------------------------------
def calculate_discount(price, discount_rate):
    """
    Calculate the discounted price of an item and the discount amount.

    Args:
        price (float): The original price of the item.
        discount_rate (float): The discount rate as a percentage.

    Returns:
        tuple: A tuple containing:
            - discounted_price (float): The price after applying the discount.
            - discount_amount (float): The amount of discount applied.
    """
    # Calculate the discount amount by multiplying the price with the discount rate
    # and dividing by 100 to convert the percentage to a decimal.
    discount_amount = price * discount_rate / 100
    
    # Subtract the discount amount from the original price to get the final price.
    discounted_price = price - discount_amount
    
    # Return both the discounted price and the discount amount as a tuple.
    return discounted_price, discount_amount
# ---------------------------------------------------
# Test the functions
# ---------------------------------------------------
if __name__ == "__main__":
    price = 1000
    discount = 10

    print("AI Version:", calculate_discount_ai(price, discount))
    print("Manual Version:", calculate_discount_manual(price, discount))
    print("Google Docstring Version:", calculate_discount_google(price, discount))
    print("NumPy Docstring Version:", calculate_discount_numpy(price, discount))
    discounted_price, discount_amount = calculate_discount(price, discount)
    print("New Function Version: Discounted Price:", discounted_price, "Discount Amount:", discount_amount)

price = 1000
discount_rate = 20

discounted_price, discount_amount = calculate_discount(price, discount_rate)
print(f"Discounted Price: {discounted_price}")
print(f"Discount Amount: {discount_amount}")