def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# So basically creating a function of Function is concept of Decorator
# In above example - say_hello function is taken as argument in my_decorator
# we are modifying the say hello function, 
# Decorators are used to modify the existing function without change in code