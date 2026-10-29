"""
Provides mock order data and the simulated database for barcode costs.
"""
from datetime import datetime, timedelta
from .models import ProductCost, Order, OrderItem

# In-memory mock database
COST_DB = {
    "BC1001": ProductCost("BC1001", "Wireless Mouse", 50.0, 5.0, 2.0),
    "BC1002": ProductCost("BC1002", "Mechanical Keyboard", 150.0, 10.0, 5.0),
    "BC1003": ProductCost("BC1003", "Laptop Stand", 80.0, 8.0, 3.0),
}

def generate_mock_orders() -> list[Order]:
    base_date = datetime(2023, 10, 1)
    orders = []
    
    order_configs = [
        ("ORD001", 0, [("BC1001", 1, 120.0, 0.15, 15.0)]),
        ("ORD002", 1, [("BC1002", 1, 350.0, 0.12, 20.0)]),
        ("ORD003", 2, [("BC1001", 2, 120.0, 0.15, 15.0), ("BC1003", 1, 180.0, 0.15, 25.0)]),
        ("ORD004", 5, [("BC1003", 2, 180.0, 0.15, 20.0)]),
        ("ORD005", 8, [("BC1002", 1, 340.0, 0.12, 25.0)]),
    ]

    for o_id, day_offset, items_data in order_configs:
        items = [OrderItem(bc, qty, price, comm, ship) for bc, qty, price, comm, ship in items_data]
        orders.append(Order(o_id, base_date + timedelta(days=day_offset), items, 0.02))
        
    return orders