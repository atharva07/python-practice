'''
Procedural Programming is a paradigm that focuses on writing procedures or routines to operate on data.
Where code is written as a sequence of steps (procedures)
Think - 1. Do this, 2. Do that, 3. Do something else
'''

def calculate_total(price, tax):
    total = price + (price * tax)
    return total

print(calculate_total(100, 0.05))