from timeit import timeit


def recurs(stop, a=0, b=1, i=2):
    if i > stop:
        return b
    else:
        return recurs(stop, a=b, b=a+b, i=i+1)


def closure():
    res = {0: 0, 1: 1}
    a, b = 0, 1
    i = 2
    def wrapped(n):
        nonlocal a, b, i
        if res.get(n):
            return res.get(n)
        a, b = b, b+a
        res[i] = b
        i += 1
        return wrapped(n)
    return wrapped


test1 = '''
def closure():
    res = {0: 0, 1: 1}
    a, b = 0, 1
    i = 2
    def wrapped(n):
        nonlocal a, b, i
        if res.get(n):
            return res.get(n)
        a, b = b, b+a
        res[i] = b
        i += 1
        return wrapped(n)
    return wrapped
x = closure()
x(500)'''
res_test1 = timeit(stmt=test1, number=500)
print(res_test1)
test2 = '''
def recurs(stop, a=0, b=1, i=2):
    if i > stop:
        return b
    else:
        return recurs(stop, a=b, b=a+b, i=i+1)

recurs(500)'''
res_test2 = timeit(stmt=test2, number=500)
print(res_test2)
