from types import SimpleNamespace

car1 = SimpleNamespace(
    color="red",
    mileage=600,
    automatic=True,
)
print(car1)

car1.mileage = 12
car1.windshield = "broken"
del car1.automatic
print(car1)
