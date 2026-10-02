# this is using Default Arguments, This mimics method overloading
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c
    
obj = Calculator()
print(obj.add(2,3))
print(obj.add(2,3,4))