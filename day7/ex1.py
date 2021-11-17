def gener(num, func):
    def wrapped(repeat):
        nonlocal num, func
        for i in range(repeat):
            if func(i):
                yield i
    return wrapped


x = gener(1, lambda x: x % 2 == 0)
print(list(x(10)))