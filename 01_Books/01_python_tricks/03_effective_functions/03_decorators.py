import functools


def null_decorator(func):
    return func


#######################################
def upper_case_decorator(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        return original_result.upper()

    return wrapper


@upper_case_decorator
def greet():
    return "Hello!"


print(greet())


############ Applying Multiple Decorators to a Function ############
def strong(func):
    @functools.wraps(func)
    def wrapper():
        return f"<strong>{func()}</strong>"

    return wrapper


def emphasis(func):
    @functools.wraps(func)
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper


@strong
@emphasis
def greet_v2():
    return "Hello!"


print(greet_v2())


############ Decorating Functions That Accept Arguments ############
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}() with {args}, {kwargs}")
        original_result = func(*args, **kwargs)

        print(f"TRACE: {func.__name__}() returned {original_result!r}")
        return original_result

    return wrapper


@trace
def say(name, line):
    return f"{name}: {line}"


say("Jane", "Hello, World!")
