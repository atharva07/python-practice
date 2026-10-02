# try:
#     num = int("123")
# except ValueError:
#     print("Invalid Number")

print("--------- Custom Exception --------------")
try:
    a = int(input())
    print(10/a)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot divide by zero")

print("---------- Custom Exceptions --------------")
class InvalidAgeException(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeException("Invalid Age")
    return True

try:
    check_age(17)
except InvalidAgeException as e:
    print(e)