# Learn functions and a basic understanding of object-oriented programming (classes and objects).

from typing import List

# Create a class named 'Product' with attributes and methods
class Product:
    """Represents a general product with a name and a price."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def get_price(self) -> float:
        """Returns the price of the product."""
        return self.price

    def set_price(self, new_price: float) -> None:
        """Sets a new price for the product."""
        self.price = new_price

# Demonstrate class inheritance
class ElectronicProduct(Product):
    """Represents an electronic product, inheriting from Product and adding a brand."""

    def __init__(self, name: str, price: float, brand: str) -> None:
        super().__init__(name, price)
        self.brand = brand

    def get_brand(self) -> str:
        """Returns the brand of the electronic product."""
        return self.brand

def main() -> None:
    """Main function to demonstrate the usage of classes and objects."""

    # Create instances (objects) of the Product class
    product1 = Product("Laptop", 1200)
    product2 = Product("Mouse", 25)
    product3 = Product("Keyboard", 75)
    product4 = Product("Monitor", 300)
    product5 = Product("Webcam", 50)

    # Access and modify attributes
    print(f"Product 1: {product1.name}, Price: {product1.get_price()}")
    product1.set_price(1250)
    print(f"Product 1 new price: {product1.get_price()}")

    print(f"Product 2: {product2.name}, Price: {product2.get_price()}")
    print(f"Product 3: {product3.name}, Price: {product3.get_price()}")
    print(f"Product 4: {product4.name}, Price: {product4.get_price()}")
    print(f"Product 5: {product5.name}, Price: {product5.get_price()}")

    # Create a list of products
    products: List[Product] = [product1, product2, product3, product4, product5]

    # Calculate the total price of all products
    total_price = sum(product.get_price() for product in products)
    print(f"Total price of all products: {total_price}")

    # Find the most expensive product
    most_expensive = max(products, key=lambda product: product.get_price())
    print(f"Most expensive product: {most_expensive.name} with price {most_expensive.get_price()}")

    # Find the least expensive product
    least_expensive = min(products, key=lambda product: product.get_price())
    print(f"Least expensive product: {least_expensive.name} with price {least_expensive.get_price()}")

    # Filter products with price greater than 100
    expensive_products = [product for product in products if product.get_price() > 100]
    print("Products with price greater than 100:")
    for product in expensive_products:
        print(f"{product.name}: {product.get_price()}")

    # Sort products by price
    sorted_products = sorted(products, key=lambda product: product.get_price())
    print("Products sorted by price:")
    for product in sorted_products:
        print(f"{product.name}: {product.get_price()}")

    # Update prices by applying a discount
    discount_percentage = 10  # 10% discount
    for product in products:
        new_price = product.get_price() * (1 - discount_percentage / 100)
        product.set_price(new_price)

    print("Prices after applying 10% discount:")
    for product in products:
        print(f"{product.name}: {product.get_price()}")

    # Create an instance of ElectronicProduct
    electronic_product = ElectronicProduct("Smartphone", 800, "TechBrand")
    print(f"Electronic Product: {electronic_product.name}, Brand: {electronic_product.get_brand()}, Price: {electronic_product.get_price()}")

    # Modify the price of the electronic product
    electronic_product.set_price(750)
    print(f"Electronic Product new price: {electronic_product.get_price()}")

    # Add the electronic product to the products list
    products.append(electronic_product)

    # Calculate the total price of all products including the electronic product
    total_price = sum(product.get_price() for product in products)
    print(f"Total price of all products including electronic product: {total_price}")

    # Sort products by price again after adding the electronic product
    sorted_products = sorted(products, key=lambda product: product.get_price())
    print("Products sorted by price after adding electronic product:")
    for product in sorted_products:
        print(f"{product.name}: {product.get_price()}")

    # Apply a different discount to electronic products
    electronic_discount_percentage = 15  # 15% discount for electronic products
    for product in products:
        if isinstance(product, ElectronicProduct):
            new_price = product.get_price() * (1 - electronic_discount_percentage / 100)
            product.set_price(new_price)

    print("Prices after applying 15% discount to electronic products:")
    for product in products:
        print(f"{product.name}: {product.get_price()}")

if __name__ == "__main__":
    main()
