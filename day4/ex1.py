class Rectangle:
    """
    class defines Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() < other.get_area()

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() == other.get_area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() <= other.get_area()

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() >= other.get_area()

    def __neg__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() != other.get_area()

    def __str__(self):
        return f'width: {self.width}, height: {self.height}'


x = Rectangle(10, 15)
print(x.get_area())
y = Rectangle(20, 40)
print(y.get_area())

print(x < y)