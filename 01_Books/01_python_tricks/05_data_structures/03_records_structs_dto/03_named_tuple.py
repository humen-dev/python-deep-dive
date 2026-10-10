from collections import namedtuple
from sys import getsizeof
from typing import NamedTuple

Point = namedtuple("Point", "x y z")
p1 = Point(1, 2, 3)
p2 = (1, 2, 3)

print(getsizeof(p1))
print(getsizeof(p2))

Car = namedtuple("Car", "color mileage automatic")
car1 = Car("red", 3812.4, True)
print(car1)


class CarTyped(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car1 = Car("red", 3812.4, True)
print(car1)
