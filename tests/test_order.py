# tests/test_order.py

import unittest
from app.order import Order
from app.user import User
from app.product import Product

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.orders = []
        User.users = {}
        Product.products = {}

    def test_place_order(self):
        User.register("user1", "password1")
        Product.add_product(1, "Product1", 100)
        self.assertTrue(Order.place_order("user1", 1))
        self.assertFalse(Order.place_order("user2", 1))  # Nonexistent user
        self.assertFalse(Order.place_order("user1", 2))  # Nonexistent product

    def test_get_orders(self):
        User.register("user1", "password1")
        Product.add_product(1, "Product1", 100)
        Order.place_order("user1", 1)
        self.assertEqual(len(Order.get_orders("user1")), 1)
        self.assertEqual(len(Order.get_orders("user2")), 0)

if __name__ == '__main__':
    unittest.main()
