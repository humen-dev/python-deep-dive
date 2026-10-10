def add(x, y):
    return x + y


print(add(1, 2))

tuples = [(1, "d"), (2, "b"), (4, "a"), (3, "c")]

a = sorted(tuples, key=lambda x: x[1])

b = sorted(range(-5, 6), key=lambda x: x * x)
