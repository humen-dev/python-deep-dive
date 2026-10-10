from collections import ChainMap, OrderedDict, defaultdict
from types import MappingProxyType

phonebook = {
    "bob": 7387,
    "alice": 3799,
    "jack": 7052,
}

squares = {x: x * x for x in range(6)}
print(squares)


d = OrderedDict(one=1, two=2, three=3)
# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd = defaultdict(list)
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")


# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = ChainMap(dict1, dict2)


# The proxy is read-only:
writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)
# read_only['one'] = 23 'mappingproxy' object does not support item assignment"
