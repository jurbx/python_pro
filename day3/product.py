class Product:
    """
    Class describe Products
    """
    products = {}

    def __init__(self, name, weight, price=0.0):
        if not isinstance(price, (int, float)):
            raise TypeError(f'{type(price).__name__} object cannot be interpreted')
        if price <= 0:
            raise ValueError('')
        self.name = name
        self.weight = weight
        self.price = price
        Product.products[name] = [weight, price]

    def __str__(self):
        return f'Name: {self.name}, Weight: {self.weight}, Price: {self.price}'


