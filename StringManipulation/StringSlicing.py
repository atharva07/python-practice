s = "automation"

print(s[0])
print(s[1])
print(s[-1])
print(s[0:4])
print(s[:4])
print(s[4:])
print(s[::-1])

print(s.find("auto"))

data = "QA,API,UI"

print(data.split(","))
print(",".join(["QA","API"]))

string = "I love coding very much"
words = string.split(' ')
print(words)

string1 = "Atharva"
print(string1[::-1])

string2 = "Hello World"
words = string2.split(' ')
reversed_words = words[::-1]
reversed_string = ' '.join(reversed_words)
print(reversed_string)

res = []
for word in words:
    rev_word = word[::-1]
    res.append(rev_word)

print(' '.join(res))
string1 = "Atharva Hiwase"
words = string1.split(" ")
for word in words:
    print(word[1:])


print("-------- different for loops ------------")

string = "Atharva"
for char in string:
    print(char)

for i in range(len(string)):
    print(string[i])

for i, char in enumerate(string):
    print(f"Index: {i}, Character: {char}")

for char in reversed(string):
    print(char)

for char in string[::-1]:
    print(char)