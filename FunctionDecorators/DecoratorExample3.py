def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello there")

say_hello()