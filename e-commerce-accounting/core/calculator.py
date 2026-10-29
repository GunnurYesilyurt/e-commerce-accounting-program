"""
Maps barcode costs to orders, calculates total revenues, expenses, and net profit.
"""
from datetime import datetime
from typing import List, Dict
from .models import Order, ProductCost

class FinancialEngine:
    def __init__(self, cost_db: Dict[str, ProductCost]):
        self.cost_db = cost_db

    def calculate_summary(self, orders: List[Order], start_date: datetime, end_date: datetime) -> dict:
        summary = {
            "total_revenue": 0.0, "total_product_cost": 0.0, "total_packaging_cost": 0.0,
            "total_commission": 0.0, "total_shipping": 0.0, "total_withholding_tax": 0.0,
            "total_other_expenses": 0.0, "net_profit": 0.0, "profit_margin": 0.0
        }

        filtered = [o for o in orders if start_date.date() <= o.date.date() <= end_date.date()]

        for order in filtered:
            for item in order.items:
                revenue = item.sale_price * item.quantity
                summary["total_revenue"] += revenue
                summary["total_commission"] += revenue * item.commission_rate
                summary["total_shipping"] += item.shipping_fee
                summary["total_withholding_tax"] += revenue * order.withholding_tax_rate

                cost_card = self.cost_db.get(item.barcode)
                if cost_card:
                    summary["total_product_cost"] += cost_card.product_cost * item.quantity
                    summary["total_packaging_cost"] += cost_card.packaging_cost * item.quantity
                    summary["total_other_expenses"] += cost_card.other_expenses * item.quantity

        total_expenses = sum([summary[k] for k in summary if k not in ("total_revenue", "net_profit", "profit_margin")])
        summary["net_profit"] = summary["total_revenue"] - total_expenses
        if summary["total_revenue"] > 0:
            summary["profit_margin"] = (summary["net_profit"] / summary["total_revenue"]) * 100

        return summary