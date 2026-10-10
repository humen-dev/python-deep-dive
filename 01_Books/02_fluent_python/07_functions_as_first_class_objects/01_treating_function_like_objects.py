def factorial(n):
    """returns the factorial of n"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
fact = factorial
print(fact)
l = list(map(factorial, range(11)))
print(l)


# Higher-Order Functions
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
def reverse(word):
    return word[::-1]

print(sorted(fruits, key=reverse))
