def tags(mapping):
    def decorator(func):
        def wrapped(*args, **kwargs):
            res = []
            for item in func(*args, **kwargs):
                if mapping(item):
                    res.append(item)
            return res
        return wrapped
    return decorator


@tags(lambda x: x % 2 == 0)
def listing(list):
    return list


x = [i for i in range(100)]
print(list(listing(x)))