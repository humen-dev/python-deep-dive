import array

########## list ##########
arr = ["one", "two", "three"]


########## tuple ##########
arr_2 = "one", "two", "three"


########## array.array: Basic Typed Arrays ##########
arr_3 = array.array("f", (1.0, 1.5, 2.0, 2.5))
arr_3[1] = 23.0
del arr[1]
# Arrays are typed
arr[1] = "hello"  # TypeError: "must be real number, not str"


########## str: Immutable Arrays of Unicode Characters ##########
# Strings are immutable:
str_arr = "abcd"
print(arr[1])
# Strings are immutable:
# str_arr[1] = 'e' Error
# del arr[1] Error


########## bytes ##########
byte_arr_str = bytes((0, 1, 2, 3))
print(byte_arr_str)  # b'x00x01x02x03'

# Only valid "bytes" are allowed:
# bytes((0, 300))

# Bytes are immutable:
# arr[1] = 23 TypeError:
# del arr[1] TypeError:


########## bytearray ##########
byte_arr = bytearray((0, 1, 2, 3))
print(byte_arr)  # bytearray(b'x00x01x02x03')
# Bytearrays are mutable:
byte_arr[1] = 23
del byte_arr[1]
byte_arr.append(42)

# byte_arr[1] = 'hello'  -> Error
# byte_arr[1] = 300    -> Error
