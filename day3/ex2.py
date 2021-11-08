from product import Product

obj1 = Product('Bread', 20, 120)
obj2 = Product('Lemon', 5, 50)
obj3 = Product('Cheese', 40, 100)


class Order:
    """
    class defines order
    """
    orders = []
    count = 0

    def __init__(self, product_name, name, phone):
        if product_name not in Product.products:
            raise TypeError('Incorrect product name')

        self.customer_name = name
        self.customer_phone = phone
        self.product_name = product_name
        self.weight = Product.products[product_name][0]
        self.price = Product.products[product_name][1]

        Order.orders.append([self.customer_name, self.customer_phone, self.product_name,
                             self.weight, self.price])
        try:
            if Order.count > 10:
                raise ValueError('Order count mustn`t be more than 10')
        except ValueError as err:
            raise err
        else:
            Order.count += 1

    def __str__(self):
        return f'Product name: {self.product_name}, Weight: {self.weight}, Price: {self.price},' \
               f' Customer name: {self.customer_name}, Customer phone: {self.customer_phone}'

    def total_price(self):
        res = 0
        for i in range(len(Order.orders)):
            res += Order.orders[i][4]
        return f'Total price = {res}'


order1 = Order('Cheese', 'Dan', '+380686665147')
order2 = Order('Bread', 'Dan', '+380686665147')
order3 = Order('Bread', 'Dan', '+380686665147')
order4 = Order('Bread', 'Dan', '+380686665147')

print(order1)
print(order2)
print(order1.total_price())

