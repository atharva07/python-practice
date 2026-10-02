class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person : {self.name}"

p1 = Person("Atharva")
print(p1.name)

# Operator Overloading
# Add dunder method only takes 2 parameters, self and other
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print(f"Adding {self.value} + {other.value}")
        return Number(self.value + other.value)
    
n1 = Number(20)
n2 = Number(20)
n3 = Number(30)

print((n1 + n2 + n3).value)

''' 
Python evaluates expressions from left to right, so it first computes n1 + n2, 
which results in a new Number object with a value of 40. Then, it takes that result and adds it to n3.
Each call handle only two operands, so the expression is evaluated in a left-associative manner.
'''