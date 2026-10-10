def yell(text: str):
    return text.upper() + "!"


print(yell("hello"))

bark = yell

del yell
# yell('hello') NameError

print(bark("hello"))

print(bark.__name__)

# Functions Can Be Stored in Data Structures
funcs = [bark, str.lower, str.capitalize]

print(funcs)


for f in funcs:
    print(f, f("hey there"))


# Functions Can Be Passed to Other Functions
def greet(func):
    greeting = func("Hi, I am a Python program")
    print(greeting)


greet(bark)


# Functions Can Be Nested
def speak(text):
    def whisper(t):
        return t.lower() + "..."

    return whisper(text)


print(speak("Hello, World"))


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + "..."

    def yell(text):
        return text.upper() + "!"

    if volume > 0.5:
        return yell

    return whisper


f1 = get_speak_func(0.3)
f2 = get_speak_func(0.7)


# Functions Can Capture Local State
def get_speak_func_better(text, volume):
    def whisper():
        return text.lower() + "..."

    def yell():
        return text.upper() + "!"

    if volume > 0.5:
        return yell

    return whisper


res = get_speak_func_better("Hello, World", 0.7)()  # HELLO, WORLD!


def make_adder(n):
    def add(x):
        return x + n

    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)
r1 = plus_3(4)  # 7
r2 = plus_5(4)  # 9


# Objects Can Behave Like Functions
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
r3 = plus_3(4)  # 7
