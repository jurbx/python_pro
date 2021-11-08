class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.get_volume() > other.get_volume()

    def __lt__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.get_volume() < other.get_volume()

    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.get_volume() == other.get_volume()

    def __le__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.get_volume() <= other.get_volume()

    def __ge__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.get_volume() >= other.get_volume()

    def __neg__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.get_volume() != other.get_volume()

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}, volume = {self.get_volume()}'


x = Box(1, 2, 7)
print(x.get_volume())
y = Box(1, 2, 8)
print(y.get_volume())

print(x > y)
