# app/product.py

class Product:
    products = {}

    @staticmethod
    def add_product(product_id, name, price):
        if product_id in Product.products:
            return False
        Product.products[product_id] = {'name': name, 'price': price}
        return True

    @staticmethod
    def get_product(product_id):
        return Product.products.get(product_id)
