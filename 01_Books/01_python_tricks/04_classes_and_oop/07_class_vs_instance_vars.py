class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


print(CountedObject.num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject.num_instances)
