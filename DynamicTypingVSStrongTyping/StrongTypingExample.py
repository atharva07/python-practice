'''
Python is also Strong Typed, meaning it does not automatically convert incompatible types.
For example, if you try to add a string and an integer, it will raise a TypeError.
'''

x = 10
y = "20"

z = x + y 
print(z) 

'''
To fix this you have to convert them explicitly to the same type, either both to string or both to integer.
'''

a = 14
b = "23"

c = a + int(b)
print(c)