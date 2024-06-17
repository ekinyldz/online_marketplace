# tests/test_integration.py

import unittest
from app.user import User
from app.product import Product
from app.order import Order

class TestIntegration(unittest.TestCase):
    def setUp(self):
        User.users = {}
        Product.products = {}
        Order.orders = []

    def test_user_product_order_integration(self):
        # Register user
        self.assertTrue(User.register("user1", "password1"))
        
        # Add product
        self.assertTrue(Product.add_product(1, "Product1", 100))
        
        # Place order
        self.assertTrue(Order.place_order("user1", 1))
        
        # Check orders
        orders = Order.get_orders("user1")
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]['product_id'], 1)

if __name__ == '__main__':
    unittest.main()
