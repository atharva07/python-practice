# Packing is usually putting multiple values into a single variable.
# Usually a tuple
a = 1, 2, 3
print(a)

def func(*args):
    print(args)

func(1, 2, 3)

def func(**kwargs):
    print(kwargs)

func(name="Atharva", age=25)