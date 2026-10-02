class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age): # constructor method
        self.name = name # Instance Attributes
        self.age = age

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
buddy = Dog("Buddy", 5)
print(buddy.speak("Woof"))