"""
2.4 Underscores, Dunders, and More
-----------------------------------
• Single Leading Underscore: _var
• Single Trailing Underscore: var_
• Double Leading Underscore: __var
• Double Leading and Trailing Underscore: __var__
• Single Underscore: _
"""


# 1. Single Leading Underscore: _var
class Test:
    def __init__(self):
        self.foo = 11  # public
        self._bar = 23  # private
        self.__baz = 23  # name mangling


# module example
def external_func():
    return 23


def _internal_func():
    return 42


# 2. Single Trailing Underscore: “var_”
def make_object(name, class_):
    pass


# 3. Double Leading Underscore: “__var” (name mangling)
t = Test()
print(dir(t))


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = "overridden"
        self._bar = "overridden"
        self.__baz = "overridden"


t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
# print(t2.__baz) # ExtendedTest' object has no attribute '__baz'


class ManglingTest:
    def __init__(self):
        self.__mangled = "hello"

    def get_mangled(self):
        return self.__mangled


ManglingTest().get_mangled()
# ManglingTest().__mangled  AttributeError: "'ManglingTest' object has no attribute '__mangled'"


class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()


# MangledMethod().__method() AttributeError: 'MangledMethod' object has no attribute '__method'
MangledMethod().call_it()


_MangledGlobal__mangled = 23


class MangledGlobal:
    def test(self):
        return __mangled


print(MangledGlobal().test())  # output 23


# 4. Double Leading and Trailing Underscore: “__var__”
class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42


print(PrefixPostfixTest().__bam__)


# 5. Single Underscore: “_”
for _ in range(32):
    print("Hello, World.")

car = ("red", "auto", 12, 3812.4)
color, _, _, mileage = car
