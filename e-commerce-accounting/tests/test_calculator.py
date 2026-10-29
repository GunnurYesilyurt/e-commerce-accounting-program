"""
Validates that the FinancialEngine correctly maps barcodes, 
filters by date, and calculates financial metrics accurately.
"""
import unittest
from datetime import datetime
from core.models import ProductCost, Order, OrderItem
from core.calculator import FinancialEngine

class TestFinancialEngine(unittest.TestCase):
    def setUp(self):
        self.cost_db = {
            "TEST_BC": ProductCost("TEST_BC", "Test Prod", 50.0, 5.0, 0.0)
        }
        self.engine = FinancialEngine(self.cost_db)
        self.orders = [
            Order("O1", datetime(2023, 1, 5), [OrderItem("TEST_BC", 2, 100.0, 0.10, 10.0)], 0.01)
        ]

    def test_calculation_accuracy(self):
        # 2 items * 100 = 200 Revenue
        # Costs: Product(2*50=100), Pkg(2*5=10)
        # Commission: 200 * 0.10 = 20
        # Shipping: 10
        # Tax: 200 * 0.01 = 2
        # Total Expenses: 100 + 10 + 20 + 10 + 2 = 142
        # Net Profit: 200 - 142 = 58
        
        summary = self.engine.calculate_summary(self.orders, datetime(2023, 1, 1), datetime(2023, 1, 10))
        
        self.assertEqual(summary["total_revenue"], 200.0)
        self.assertEqual(summary["total_product_cost"], 100.0)
        self.assertEqual(summary["total_commission"], 20.0)
        self.assertEqual(summary["net_profit"], 58.0)
        self.assertEqual(summary["profit_margin"], (58.0 / 200.0) * 100)

    def test_date_filtering(self):
        # Filtering out of range
        summary = self.engine.calculate_summary(self.orders, datetime(2023, 2, 1), datetime(2023, 2, 10))
        self.assertEqual(summary["total_revenue"], 0.0)

if __name__ == '__main__':
    unittest.main()