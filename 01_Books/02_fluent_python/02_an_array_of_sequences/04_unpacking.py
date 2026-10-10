#  parallel assignment
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # unpacking

# swap
a = 1
b = 2
b, a = a, b

# Function call
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)


# * to Grab Excess Items
a, b, *rest = range(5)
print(a, b, *rest)
a, b, *rest = range(2)
print(a, b, *rest)
a, *body, c, d = range(5)
*head, b, c, d = range(5)


# * in Function Calls and Sequence Literals
def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


print(fun(*[1, 2], 3, *range(4, 7)))

print(*range(4), 4)
print([*range(4), 4])
print({*range(4), 4, *(5, 6, 7)})


# Nested Unpacking
metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

main()

def query_returning_single_row():
    return [1]

def query_returning_single_row_with_single_field():
    return [[2]]

[record] = query_returning_single_row()
[[field]] = query_returning_single_row_with_single_field()

print(record)
print(field)
