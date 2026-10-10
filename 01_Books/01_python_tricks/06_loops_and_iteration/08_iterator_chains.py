def integers():
    yield from range(1, 9)


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
print(list(chain))
