# lab15_food_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

app = FastAPI(
    title="Online Food Ordering API",
    description="A RESTful API that simulates a basic online food ordering system.",
    version="1.0.0"
)

# ----- Data Models -----
class Dish(BaseModel):
    """Represents a menu item (dish) available for order."""
    id: int
    name: str
    price: float

class Order(BaseModel):
    """Represents a customer’s food order."""
    id: int
    items: List[int] = Field(..., description="List of dish IDs included in the order")
    status: str = Field(default="Pending", description="Current status of the order")
    total: float = 0.0

class OrderUpdate(BaseModel):
    """Represents updates that can be applied to an existing order."""
    items: Optional[List[int]] = None
    status: Optional[str] = None

# ----- In-memory databases -----
menu_db: Dict[int, Dish] = {
    1: Dish(id=1, name="Margherita Pizza", price=8.99),
    2: Dish(id=2, name="Cheeseburger", price=7.49),
    3: Dish(id=3, name="Pasta Alfredo", price=9.25),
    4: Dish(id=4, name="Caesar Salad", price=5.75),
}

orders_db: Dict[int, Order] = {}

# ----- Helper Function -----
def calculate_total(items: List[int]) -> float:
    """Calculate the total price of selected dishes."""
    total = 0.0
    for item_id in items:
        if item_id not in menu_db:
            raise HTTPException(status_code=400, detail=f"Dish ID {item_id} not found.")
        total += menu_db[item_id].price
    return round(total, 2)

# ----- API Endpoints -----

@app.get("/menu", response_model=List[Dish])
def get_menu():
    """Retrieve the list of available dishes."""
    return list(menu_db.values())


@app.post("/order", response_model=Order)
def place_order(order: Order):
    """Place a new food order."""
    if order.id in orders_db:
        raise HTTPException(status_code=400, detail="Order ID already exists.")
    order.total = calculate_total(order.items)
    orders_db[order.id] = order
    return order


@app.get("/order/{order_id}", response_model=Order)
def get_order(order_id: int):
    """Track the status and details of an existing order."""
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found.")
    return orders_db[order_id]


@app.put("/order/{order_id}", response_model=Order)
def update_order(order_id: int, order_update: OrderUpdate):
    """Update order details (e.g., change items or status)."""
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found.")
    stored_order = orders_db[order_id]

    if order_update.items:
        stored_order.items = order_update.items
        stored_order.total = calculate_total(order_update.items)

    if order_update.status:
        stored_order.status = order_update.status

    orders_db[order_id] = stored_order
    return stored_order


@app.delete("/order/{order_id}")
def cancel_order(order_id: int):
    """Cancel an existing order."""
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found.")
    del orders_db[order_id]
    return {"message": f"Order {order_id} has been cancelled successfully."}
