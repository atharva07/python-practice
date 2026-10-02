# args and kwargs - we use them when we are unsure about the number of arguments a function will take
# args - (Non Keyword Argumrnts)
# kwargs - (Keyword Arguments)

def smart_divide(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@smart_divide
def divide(a, b):
    return a/b

#Test
result = divide(10, 2)
print(f"Final result: {result}") 