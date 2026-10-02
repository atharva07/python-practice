def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class logger:
    pass

l1 = logger()
l2 = logger()

print(l1 is l2)

# so the singleton pattern ensures that only one instance of a class is created
# and provides a global point of access to that instance.
# here we are using a decorator to implement the singleton pattern.