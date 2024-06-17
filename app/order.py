# app/order.py

from .user import User
from .product import Product

class Order:
    orders = []

    @staticmethod
    def place_order(username, product_id):
        if username not in User.users or product_id not in Product.products:
            return False
        Order.orders.append({'username': username, 'product_id': product_id})
        return True

    @staticmethod
    def get_orders(username):
        return [order for order in Order.orders if order['username'] == username]
