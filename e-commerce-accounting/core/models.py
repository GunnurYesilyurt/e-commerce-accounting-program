"""
Defines the object-oriented structure for Products, Orders, and Items.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class ProductCost:
    barcode: str
    product_name: str
    product_cost: float
    packaging_cost: float
    other_expenses: float

@dataclass
class OrderItem:
    barcode: str
    quantity: int
    sale_price: float
    commission_rate: float
    shipping_fee: float

@dataclass
class Order:
    order_id: str
    date: datetime
    items: List[OrderItem]
    withholding_tax_rate: float