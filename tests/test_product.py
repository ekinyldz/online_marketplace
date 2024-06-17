# tests/test_product.py

import unittest
from app.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        Product.products = {}

    def test_add_product(self):
        self.assertTrue(Product.add_product(1, "Product1", 100))
        self.assertFalse(Product.add_product(1, "Product1", 100))  # Duplicate

    def test_get_product(self):
        Product.add_product(1, "Product1", 100)
        self.assertIsNotNone(Product.get_product(1))
        self.assertIsNone(Product.get_product(2))

if __name__ == '__main__':
    unittest.main()
