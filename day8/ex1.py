def decorator(func):
    i = 0

    def wrapped(*args, **kwargs):
        nonlocal i
        i += 1
        return f'{func(*args, **kwargs)}, {i}'
    return wrapped


@decorator
def func(hello):
    return hello


for i in range(10):
    print(func('Hello'))
