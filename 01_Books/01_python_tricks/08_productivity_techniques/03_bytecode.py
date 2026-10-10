import dis


def greet(name):
    return f"Hello {name}"


print(greet.__code__.co_code)
print(greet.__code__.co_consts)
print(greet.__code__.co_varnames)


dis.dis(greet)
