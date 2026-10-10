from collections import namedtuple

Car = namedtuple("Car", ("color", "mileage"))
my_car = Car("red", 3812.4)
print(my_car.color)
print(my_car.mileage)

color, mileage = my_car
print(color, mileage)
print(my_car)


########## Subclassing Namedtuples ##########
class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == "red":
            return "#ff0000"

        return "#000000"


c = MyCarWithMethods("red", 1234)
print(c.hexcolor())

dict_obj = my_car._asdict()
