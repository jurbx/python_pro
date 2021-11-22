from timeit import timeit

def rep(repeat: int, file: str):

    def decorator(func):
        def wrapped(*args, **kwargs):
            res = timeit(stmt=f'{func(*args, **kwargs)}', number=repeat)
            doc = open(file, 'w')
            doc.write(f'{res}')
            return func(*args, **kwargs)
        return wrapped
    return decorator


@rep(5000, 'test')
def iteration(repeat1):
    x = []
    for i in range(repeat1):
        x.append(i)
    return x


x = iteration(10000)
print(x)
