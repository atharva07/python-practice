from itertools import count, cycle, repeat, groupby

for i in count(5, 2):
    if i > 15:
        break
    print(i)

c = cycle(['A', 'B', 'C'])
for i in range(5):
    print(next(c))

for i in repeat("test", 3):
    print(i)

res = []
data = [1,1,2,2,2,3]
for key, group in groupby(data):
    count = len(list(group))
    print(key, count)
    res.append((count, int(key)))

print(res)

words = ["apple", "bat", "ball", "cat", "car"]
# Sort by first letter
words.sort(key=lambda x: x[0])

for key, group in groupby(words, key = lambda x: x[0]):
    print(key, list(group))   

print("--------- Complex Example ------------")
num_list = [1,2,3,4,5,6]

k = 2
for i in range(0, len(num_list), k):
    group = num_list[i:i+k]
    result = group[::-1]
    print(result)

