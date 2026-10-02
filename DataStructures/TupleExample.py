coordinate = (10, 20)
colors = ('red','green','blue')
single_element = (42,)

# Accessing Element
x,y = coordinate
print(x)
print(y)

print(colors[1])

# This is will raise an error as tuples are immutable
colors[1] = "yellow"
print(colors)

def get_usr_info():
    return "John", 30, "Engineer"

name, age, job = get_usr_info()