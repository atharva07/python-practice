class Dog:
    def speak(self):
        return "Woof"
    
dog = Dog()

print(dog.speak())

# With using monkey patching
def new_speak():
    return "Meow"

# We modified the speak method at runtime without changing the original class definition
dog.speak = new_speak

print(dog.speak())