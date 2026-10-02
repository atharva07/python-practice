''' Generator is a simpler way to create iterator using yield '''
def counter(max):
    current = 0
    while current <= max:
        current += 1
        yield current

for num in counter(5):
    print(num)

''' Generator are special type of iterators in python. They automatically implement the iterator protocol '''

def counter(max):
    current = 0
    while current <= max:
        current += 1
        yield current

for num in counter(10):
    print(num)