import array

symbols = "$¢£¥€¤"
print(tuple(ord(symbol) for symbol in symbols))


print(array.array("I", (ord(symbol) for symbol in symbols)))

colors = ["black", "white"]
sizes = ["S", "M", "L"]
for tshirt in (f"{c} {s}" for c in colors for s in sizes):
    print(tshirt)
