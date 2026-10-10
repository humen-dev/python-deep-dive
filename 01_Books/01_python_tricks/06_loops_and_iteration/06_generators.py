class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


def repeater(value):
    while True:
        yield value


generator_obj = repeater("Hey")
print(next(generator_obj))


def repeat_three_times(value):
    yield value
    yield value
    yield value


for x in repeat_three_times("Hey there"):
    print(x)


def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value
