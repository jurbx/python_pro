def decorator(func):
    def wrapped(*args, **kwargs):
        doc = open(f'{Text.__name__}', 'w')
        doc.write(f'{func(*args, **kwargs)}')
        doc.close()
        return func(*args, **kwargs)
    return wrapped


class Text:
    def __init__(self, a):
        self.a = a

    @decorator
    def __str__(self):
        return self.a


x = Text('Hello90432')
print(x)
