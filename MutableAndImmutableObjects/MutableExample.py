'''
Mutable Objects - Can be changed after they are created
Examples: Lists, Dictionaries, Sets
'''

# List
list1 = [1,2,3]
print(id(list1))

list1.append(4)
print(id(list1))

# Dictionary
dict1 = {"a": 1, "b" : 2}
dict1["b"] = 10

print(dict1)

# Set
set1 = {1,2,3}
print(id(set1))

set1.add(5)
print(id(set1))

# Custom Class Objects - user defined classes are mutable by default
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Atharva")
print("Before : ", p1.name)
p1.name = "John"
print("After : ", p1.name)

'''
Immutable Objects - Cannnot be changed after they are created
Examples: String, int, float, tuple, frozenset
'''

# int
x = 10
print(id(x))
x = x + 5
print(id(x))

# float
f = 1.15
print(id(f))
f = f + 0.05
print(id(f))