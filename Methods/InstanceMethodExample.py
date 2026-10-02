class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

emp = Employee("Alice", 30)
emp.display_info()

# A method that works on instance data
# Takes self as the first parameter
# Can access Instance variables