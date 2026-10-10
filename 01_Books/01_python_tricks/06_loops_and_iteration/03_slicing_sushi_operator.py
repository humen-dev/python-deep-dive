lst = [1, 2, 3, 4, 5]

start = 1
end = 3
step = 1

print(lst[start:end:step])


# reverser order
print(lst[::-1])

# remove all elements
del lst[:]

# replace elements in the list
lst = [1, 2, 3, 4, 5]
original_lst = lst
lst[:] = [7, 8, 9]

# copy list (shallow)
opied_lst = lst[:]
