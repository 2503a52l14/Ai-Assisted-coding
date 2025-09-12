class Inventory:
    """
    A class to manage inventory stock.
    """
    def __init__(self):
        self.stock = {}

    def add_item(self, item, quantity):
        """
        Adds a specified quantity of an item to the inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.stock[item] = self.stock.get(item, 0) + quantity

    def remove_item(self, item, quantity):
        """
        Removes a specified quantity of an item from the inventory.
        """
        if item not in self.stock:
            raise KeyError(f"Item '{item}' not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.stock[item] < quantity:
            raise ValueError(f"Not enough stock of '{item}' to remove")
        self.stock[item] -= quantity
        if self.stock[item] == 0:
            del self.stock[item]

    def get_stock(self, item):
        """
        Returns the current stock of an item.
        """
        return self.stock.get(item, 0)

# Test cases
inventory = Inventory()

# Test case 1: Adding items
inventory.add_item("apple", 10)
assert inventory.get_stock("apple") == 10, "Test case 1 failed"

# Test case 2: Removing items
inventory.remove_item("apple", 5)
assert inventory.get_stock("apple") == 5, "Test case 2 failed"

# Test case 3: Removing all stock of an item
inventory.remove_item("apple", 5)
assert inventory.get_stock("apple") == 0, "Test case 3 failed"

# Test case 4: Adding multiple items
inventory.add_item("banana", 20)
inventory.add_item("orange", 15)
assert inventory.get_stock("banana") == 20, "Test case 4 failed"
assert inventory.get_stock("orange") == 15, "Test case 4 failed"

# Test case 5: Removing an item not in stock
try:
    inventory.remove_item("grape", 5)
except KeyError:
    pass
else:
    assert False, "Test case 5 failed"

print("All test cases passed!")