def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(firstname="Atharva", lastname="Hiwase", Age=27, location="Nagpur")
intro(firstname="Darren", lastname="Sammy", email="darren.sammy@gmail.com", location="las vegas")

def intro(**data):
    print("\nData type of argument: ", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(firstname="Atharva", age=27)
# above kwargs is used as we are not sure about how many keyword word arguments the function is going to take