"""
Task 3: Inventory Management System
-----------------------------------
Prompt : Generate a Python program for an inventory management system that stores products with ID, name, price, and quantity.
Use efficient algorithms (like Merge Sort for sorting and Binary Search for searching).
Include docstrings explaining the algorithms and their complexities.

Scenario:
A store needs to quickly search and sort thousands of products by
different attributes using efficient algorithms.
This program demonstrates searching by ID and sorting by price/quantity.
"""

class Product:
    """Represents a product in the inventory."""
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

def binary_search_product(products, target_id):
    """Binary search for product ID (requires sorted list by ID)."""
    low, high = 0, len(products) - 1
    while low <= high:
        mid = (low + high) // 2
        if products[mid].pid == target_id:
            return products[mid]
        elif products[mid].pid < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def merge_sort_products(products, key=lambda x: x.price):
    """Sort products using Merge Sort by the given key (price or quantity)."""
    if len(products) <= 1:
        return products
    mid = len(products) // 2
    left = merge_sort_products(products[:mid], key)
    right = merge_sort_products(products[mid:], key)
    return merge_products(left, right, key)

def merge_products(left, right, key):
    """Helper to merge sorted product lists."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Test Data ---
inventory = [
    Product(101, "Pen", 10, 100),
    Product(102, "Notebook", 40, 50),
    Product(103, "Pencil", 5, 200)
]

# --- Sorting Tests ---
sorted_by_price = merge_sort_products(inventory, key=lambda x: x.price)
sorted_by_quantity = merge_sort_products(inventory, key=lambda x: x.quantity)
assert [p.name for p in sorted_by_price] == ["Pencil", "Pen", "Notebook"]
assert [p.name for p in sorted_by_quantity] == ["Notebook", "Pen", "Pencil"]

# --- Searching Tests ---
sorted_inventory = merge_sort_products(inventory, key=lambda x: x.pid)
found = binary_search_product(sorted_inventory, 102)
assert found.name == "Notebook"

# --- Output Section ---
print("Products sorted by Price:")
for p in sorted_by_price:
    print(f"{p.name} → ₹{p.price}")

print("\nProducts sorted by Quantity:")
for p in sorted_by_quantity:
    print(f"{p.name} → {p.quantity} units")

print("\nSearching for Product ID 102:")
if found:
    print(f"Found: {found.name}, Price ₹{found.price}, Quantity {found.quantity}")
else:
    print("Product not found!")

print("✅ Task 3 (Inventory Management System) executed successfully!")
# --- Inventory Management System Implementation ---