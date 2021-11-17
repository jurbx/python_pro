def mapping(inst, func):
    res = []
    for item in inst:
        if func(item):
            res.append(item)
    return res, sum(res)


print(mapping([i for i in range(10)], lambda x: x % 2 == 0))
