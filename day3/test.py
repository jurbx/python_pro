class Rectangle:
    size = []

    def __init__(self, height, width):
        self.height = height
        self.width = width
        Rectangle.size.append([height, width])

    def getarea(self):
        try:
            if not self.height < 100:
                raise ValueError(f'Invalid value height: {self.height}')
            if not self.width < 100:
                raise ValueError(f'Invalid value width: {self.width}')
        except ValueError as err:
            return err
        else:
            return f'area = {self.height * self.width}'

    def __str__(self):
        return f'width: {self.width}, height: {self.height}'


obj1 = Rectangle(10, 23)
obj2 = Rectangle(65, 34)
obj3 = Rectangle(87, 34)
obj4 = Rectangle(23, 76)
obj5 = Rectangle(12, 5)


print(Rectangle.size)