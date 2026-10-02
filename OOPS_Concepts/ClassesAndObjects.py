class Vehicle:
    def __init__(self):                         # Non Parameterized constructor
        print("Non Parameterized Constructor")

    def __init__(self, name, model):                         # Parameterized Constructor
        self.name = name
        self.model = model

    def Car(self):
        print(self.name, self.model)

    def Bike(self):
        print(self.name, self.model)

car1 = Vehicle("Alto", 2019)
car2 = Vehicle("Innova", 2020)
bike1 = Vehicle("Pulsar", 2018)

car1.Car()
car2.Car()

bike1.Bike()