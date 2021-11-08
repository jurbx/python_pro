class Person:
    """
    Method which describe person
    """
    def __init__(self, age, height, name, surname):
        self.age = age
        self.height = height
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Name = {self.name}, age = {self.age}, height = {self.height}, height = {self.surname}'
