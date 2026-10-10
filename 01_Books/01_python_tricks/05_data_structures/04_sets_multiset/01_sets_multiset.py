vowels = {"a", "e", "i", "o", "u"}
squares = {i * i for i in range(10)}
print(squares)

letters = set("alice")
res_1 = letters.intersection(vowels)
vowels.add("x")
print(len(vowels))

########## frozenset -- Immutable Sets ##########
vowels_frozen = frozenset({"a", "e", "i", "o", "u"})
# vowels_frozen.add('p') -> Error
