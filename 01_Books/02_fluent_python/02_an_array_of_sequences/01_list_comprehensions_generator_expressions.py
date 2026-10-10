symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)


codes = [ord(symbol) for symbol in symbols]
print(codes)


# using Walrus
x = 'ABC'
codes = [last := ord(c) for c in x]
print(last)



########## Listcomps Versus map and filter ##########
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))
