
def ones(*args):
    return tuple(1 for _ in args)

o = ones(1, 2, 3, 4, 5)

print(type(o), o)