# Product class
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_value(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"{self.name} - ${self.price} x {self.quantity} = ${self.calculate_value()}"


# Warehouse class
class Warehouse:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, name: str) -> bool:
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                return True
        return False

    def total_value(self) -> float:
        return sum(p.calculate_value() for p in self.products)

    def __str__(self) -> str:
        product_list = "\n".join(str(p) for p in self.products)
        return f"Warehouse Inventory:\n{product_list}\nTotal Value: ${self.total_value()}"


# Example usage
if __name__ == "__main__":
    p1 = Product("Laptop", 1000, 3)
    p2 = Product("Phone", 500, 5)

    warehouse = Warehouse()
    warehouse.add_product(p1)
    warehouse.add_product(p2)

    print(warehouse)

    # Remove product
    warehouse.remove_product("Phone")
    print("\nAfter removing Phone:\n", warehouse)
