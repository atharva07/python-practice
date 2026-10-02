fruits = ['apple', 'banana', 'cherry']
numbers = [1,2,3,4,5]
mixed = [1, 'hello', 3.14, True]

# Basic operations
fruits.append('Watermelon')
numbers.append(7)
fruits.insert(4, 'lululemon')
fruits.remove('banana')

print(fruits)
# List comprehension
squared = [x**2 for x in range(10)]
even_sqaures = [x**2 for x in range(10) if x % 2 == 0]

# slicing
numbers = [0,1,2,3,4,5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])