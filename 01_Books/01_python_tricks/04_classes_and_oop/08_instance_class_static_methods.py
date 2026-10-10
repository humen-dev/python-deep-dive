class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def class_method(cls):
        return "class method called", cls

    @staticmethod
    def staticmethod():
        return "static method called"


obj = MyClass()
print(obj.method())
print(MyClass.method(obj))
print(obj.class_method())
print(obj.staticmethod())
