lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32_450, 0.66, 8014)
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]

for passport in sorted(traveler_ids):
    print("{}/{}".format(*passport))

for country, _ in traveler_ids:
    print(country)


########## Tuples as Immutable Lists ##########
a = (10, "alpha", [1, 2])
b = (10, "alpha", [1, 2])

print(a == b)

b[-1].append(99)

print(a == b)
print(b)


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, "alpha", (1, 2))
tm = (10, "alpha", [1, 2])
fixed(tf)
