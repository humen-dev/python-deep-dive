def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo("hello")
foo("hello", 1, 2, 3)
foo("hello", 1, 2, 3, key1="value", key2=999)


############ Forwarding Optional or Keyword Arguments ############
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = "blue"


print(AlwaysBlueCar("green", 48392).color)
