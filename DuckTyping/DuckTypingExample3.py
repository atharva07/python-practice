class Human:
    def walk(self):
        print("Human walking")

class Robot:
    def walk(self):
        print("Robot walking")

class Dog:
    def make_sound(self):
        print("Woof")

def lets_walk(entity):
    entity.walk()

human = Human()
robot = Robot()
dog = Dog()

lets_walk(human) # output: Human walking
lets_walk(robot) # output: Robot walking
lets_walk(dog) # output: AttributeError: 'Dog' object has no attribute 'walk'