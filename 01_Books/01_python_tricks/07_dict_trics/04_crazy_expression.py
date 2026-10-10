d = {True: 'yes', 1: 'no', 1.0: 'maybe'}
print(d)

lst = ["no", "yes"]
print(lst[True])
print(lst[False])


class AlwaysEquals:
    def __eq__(self, other):
        return True
    def __hash__(self):
        return id(self)
