# dict Comprehensions
dial_codes = [
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (1, "United States"),
]
country_dial = {country: code for code, country in dial_codes}
print(country_dial)
country_dial = {
    code: country.upper() for country, code in sorted(country_dial.items()) if code < 70
}
print(country_dial)


# Unpacking
def dump(**kwargs):
    return kwargs


print(dump(**{"x": 1}, y=2, **{"z": 3}))
print({"a": 0, **{"x": 1}, "y": 2, **{"z": 3, "x": 4}})

# Merging Mappings with |
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
print(d1 | d2)
print(d1)
# inplace mapping
d1 |= d2
print(d1)
