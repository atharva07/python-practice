# This also mimics Method Overloading
class Calculator:
    def add(self, *numbers):
        return sum(numbers)

obj = Calculator()

print(obj.add(1,2))
print(obj.add(1,2,3,4))