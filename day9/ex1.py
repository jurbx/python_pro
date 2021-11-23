class Descriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError('method is read only')

    def __delete__(self):
        raise AttributeError('cannot delete attribute, read only')


class Main:
    def __init__(self, value, count):
        self.value = Descriptor(value)
        self.count = Descriptor(count)

    def __str__(self):
        return f'value: {self.value}, count: {self.count}'


x = Main('21', '65')
print(x)
