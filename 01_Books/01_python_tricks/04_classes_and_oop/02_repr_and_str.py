class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color!r}, {self.mileage!r})"

    def __str__(self):
        return "__str__ for Car"


my_car = Car("red", 5000)
print(my_car)
print(repr([my_car]))
