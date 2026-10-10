iterator = ('Hello' for i in range(3))
even_squares = (x * x for x in range(10) if x % 2 == 0)

# inline generators
for x in ('Bom dia' for i in range(3)):
    print(x)
