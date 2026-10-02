from abc import ABC, abstractmethod

# this is a base class, it does not have an implementation of the area method
# Any Child class that inherits from this class must implement the area method
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 2 * 2
    
c = Circle()
print(c.area())