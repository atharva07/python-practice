# this works because python is dynamically typed
class Printer:
    def show(self, value):
        if isinstance(value, int):
            print("Integer :", value)

        elif isinstance(value, str):
            print("String :", value)

        elif isinstance(value, list):
            print("List: ", value)

obj = Printer()
obj.show(10)
obj.show("Atharva")
obj.show([1,2,3])