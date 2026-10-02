def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum: ", sum)

def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print(sum)

adder(4,5)
adder(6,7,8)

def adder(*num):
    sum = 0

    for n in num:
        sum += n
    
    print(sum)

adder(4,5)
adder(4,5,6)

def person_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

person_info(name="John", age=30, city="New York")

# above args is used as we are not sure about the number of non keyword arguments function is going to take

def person_info(**info):
    for key, value in info.items():
        print(f"{key} : {value}".format(key, value))

person_info(name="Atharva", age=27, city="London")
