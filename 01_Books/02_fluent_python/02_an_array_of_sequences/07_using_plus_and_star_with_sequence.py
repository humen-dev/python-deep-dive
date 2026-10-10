"""
Using + and * with Sequences
"""
l = [1, 2, 3]
l = l * 5
print(l)
print(5 * 'abcd')

# Building Lists of Lists
board = [['_'] * 3 for i in range(3)]
board[1][2] = "X"
print(board)
print(board)


# Augmented Assignment with Sequences
l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l)) # the same ID

t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t)) # new tuple is crated


# A += Assignment Puzzler
t = (1, 2, [30, 40])
t[2] += [50, 60]
print(t)
