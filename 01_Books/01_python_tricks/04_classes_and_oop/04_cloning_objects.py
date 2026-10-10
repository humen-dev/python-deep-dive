import copy

original_list = []
original_dict = {}
original_set = set()

new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)
print("*****")
########## Making Shallow Copies ##########
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
xs.append(["new sublist"])
print(xs)
print(ys)

xs[1][0] = "X"
print(xs)
print(ys)
print("*****")
########## Making Deep Copies ##########
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
print(xs)
print(zs)
xs[1][0] = "X"
print(xs)
print(zs)
print("*****")

########## Copying Arbitrary Objects ##########


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"


a = Point(23, 42)
b = copy.copy(a)
print(a is b)


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return f"Rectangle({self.top_left!r}, {self.bottom_right!r})"


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
rect.top_left.x = 999

print(rect)
print(srect)
drect = copy.deepcopy(srect)
drect.top_left.x = 222
print(drect)
print(srect)
print(rect)
