a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

a, *b = 1, 2, 3, 4

print(a)
print(b)

def add(a, b, c):
    return a + b + c

nums = (1, 2, 3)
print(add(*nums))

def greet(name, age):
    print(name, age)

data = {"name": "Atharva", "age": 25}
greet(**data)

a = 20
b = 30

a, b = b, a
print(a)
print(b)