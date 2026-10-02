from collections import defaultdict, Counter, deque

person = {
    'name': 'Atharva',
    'age': 30,
    'city': 'Nagpur'
}

# Accessing and Modifying
print(person['name'])
person['age'] = 31
person['job'] = 'Engineer'

# Dictonary Method
keys = person.keys()
values = person.values()
items = person.items()

# Dictonary comprehension
squares = {x: x**2 for x in range(10)}
print(squares)

age = person.get('age', 'Unknown')

word_count = defaultdict(int)
for word in ['apple', 'banana', 'apple', 'cherry']:
    word_count[word] += 1

# Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
colors_count = Counter(colors)
print(colors_count.most_common(2))

print(colors_count)