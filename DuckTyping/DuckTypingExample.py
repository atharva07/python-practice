class Dog:
    def speak(self):
        return "woof"
    
class Cat:
    def speak(self):
        return "meow"
    
def make_animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_sound(dog)  
make_animal_sound(cat)

''' Duck typing in python means we don't check the type of an object explicitly. Instead
we rely on the presence of certain methods or properties to determine if an object can be used in a particular context
or whether the object supports the required methods or behavior '''

''' Duck Typing is like runtime polymorphism WITHOUT inheritence '''
# With inheritence
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
    
# Without Inheritence
class Animal:
    def speak(self):
        return "Woof"
    
class Robot:
    def speak(self):
        return "Beep"
    
def lets_speak(entity):
    print(entity.speak())

animal = Animal()
robot = Robot()
lets_speak(animal)
lets_speak(robot)

''' Polymorphism is the concept of using a common interface for different types, while duck typing is how 
python achieves polymorphism dynamically by focusing on an object's behavior rather its type '''