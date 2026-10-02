class Dog:
    def speak(self):
        return "Bark"
    
class Cat:
    def speak(self):
        return "Meow"
    
class Robot:
    def speak(self):
        return "Hello"
    
# This method will raise an error stating that it has no method 'speak'
class Mobile:
    def type(self):
        return "Typing"
    
def make_speak(obj):
    print(obj.speak())

for obj in [Dog(), Cat(), Robot(), Mobile()]:
    make_speak(obj)