# 1. Find User with Specific ID
response = {
  "users":[
    {"name":"John","id":1},
    {"name":"Sam","id":2}
  ]
}

for user in response["users"]:
    if user["id"] == 2:
        print(user)

# using list comprehensions
users = [user for user in response["users"] if user["id"] == 2]
print(users)

# 2. Get All User Names
response = {
  "users":[
    {"name":"John","id":1},
    {"name":"Sam","id":2},
    {"name":"Mike","id":3}
  ]
}

for user in response["users"]:
    print(user["name"])

names = [user["name"] for user in response["users"]]
print(names)

count = len(response["users"])
print(count)

# 3. Find Duplicate IDs

response = {
 "users":[
   {"id":1},
   {"id":2},
   {"id":1}
 ]
}

ids = [user["id"] for user in response["users"]]

duplicate = [i for i in ids if ids.count(i) > 1]
print(set(duplicate))

# 4. Check if user exists
exists = any(user["id"] == 2 for user in response["users"])
print(exists)

assert any(user["id"] == 2 for user in response["users"])

# 5. Get user with maximum ID

responsemax = {
  "users":[
    {"name":"John","id":1},
    {"name":"Sam","id":2},
    {"name":"Mike","id":3}
  ]
}

max_user = max(responsemax["users"], key = lambda x : x["id"])
print(max_user)

# 6. Filter user Id's with Id>1

print("-----------id>1--------------")
for user in responsemax["users"]:
    if user["id"] > 1:
        print(user)

filteredres = [user for user in responsemax["users"] if user["id"] > 1]
print(filteredres)

# 7. Find total order value

responseapi = {
 "orders":[
   {
     "order_id":101,
     "items":[
        {"name":"Laptop","price":1000},
        {"name":"Mouse","price":20}
     ]
   }
 ]
}

print("-----------total order value--------------")
total_order = 0
for order in responseapi["orders"]:
    for item in order["items"]:
        total_order += item["price"]

print(total_order) 