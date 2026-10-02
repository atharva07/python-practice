class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("I can quack like a duck")

class Car:
    pass

def make_it_quack(obj):
    if hasattr(obj, "quack"):
        obj.quack()
    else:
        print("This obj can't quack")

make_it_quack(Duck())
make_it_quack(Person())
make_it_quack(Car())