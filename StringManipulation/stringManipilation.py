import re 

string = "A man, a plan, a canal: Panama"
cleaned = re.sub(r'[^a-zA-Z0-9]', '', string)

print(cleaned)

print("------------------++-------------------------")
cleaned1 = ''.join(filter(str.isalnum, string))
print("Cleaned1:", cleaned1)

cleaned2 = ''.join(char for char in string if char.isalnum())
print("Cleaned2:", cleaned2)

string = "Let's take LeetCode contest"
words = string.split(' ')
print(words)

for word in words:
    #print(word)
    chars = list(word)
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    print(''.join(chars))

word = "connect"

string = "name2.name3.name4"

result = string.replace("name", "atharva")
print(result)

result1 = string.replace("name", "atharva", 1)
print(result1)

string = "abcdef"
print(string[:3])
print(string[3:])

string1 = "Hello"

print("------------ reverse string ---------------")
def reverseString(string):
    result = ""
    for char in string:
        result = char + result

    return result

print(reverseString(string1))

print("---------- reverse using two pointer --------------")

def reverseStringTwo(string):
    chars = list(string)
    left = 0
    right = len(string) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)

print(reverseStringTwo(string1))

stringath = "Atharva"
new_string = "Z" + stringath[1:]

print("New String = ", new_string)

string1 = "Hello this is python world"
result = string1.replace(' ', ',')
print(result)

result = ""
for char in string1:
    if char == " ":
        result += ","
    else:
        result += char

print(result)


arr1 = [1,2,3,4,5]

for i in range(len(arr1)):
    print(arr1[i])
print("-------------------")
for item in arr1:
    print(item)

print("-------------------")
# print the elements of arr in reverse
for item in arr1[::-1]:
    print(item)

string1 = "Hello"
print(list(reversed(string1)))

res = []
for char in reversed(string1):
    res.append(char)

print(''.join(res))

for i in range(3,5):
    print(i)

n = 5
for i in range(n-1, -1, -1):
    print(i)

string = "Atharva"
for i in range(len(string)-1, -1, -1):
    print(string[i])

string = "Atharva"
for i in range(len(string)-1, -1, -1):
    print(string[i], end="")

print("------------------")

string = "I am tron"
for i in range(len(string)-1, -1, -1):
    print(string[i], end="")

print("====================")
number = 1231434
res = ""

for digit in str(number):
    res = digit + res

print(int(res))

nums = [1,1,2,3,4,4,5]
res = []

for num in nums:
    if num not in res:
        res.append(num)

print(res)