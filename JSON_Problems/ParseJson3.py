# Question: Given API Logs, return top K most frequent users.
from typing import Counter

logs = ["u1","u2","u1","u3","u2","u1"]
k = 2

freq = Counter(logs)

for key, value in freq.most_common(k):
    print(key, value)

# Goal: Convert to -> id age city
response = {
 "users":[
   {"id":1,"details":{"age":25,"city":"NY"}},
   {"id":2,"details":{"age":30,"city":"LA"}}
 ]
}

result = []
for user in response["users"]:
    flattened = {
        "id": user["id"],
        "age": user["details"]["age"],
        "city": user["details"]["city"]
    }
    result.append(flattened)

print(result)