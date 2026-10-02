class Calculator1:
    def Sum(self, a, b):
        return a+b
    
class Calculator2:
    def Multiplication(self, a, b):
        return a*b
    
class Derived(Calculator1, Calculator2):
    def Divide(self, a, b):
        return a/b
    
d = Derived()
print(d.Sum(10,12))
print(d.Multiplication(3,4))
print(d.Divide(8,2))