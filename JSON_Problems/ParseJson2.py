# Question: Verify that user with id = 2 exists.

response1 = {
"users":[
        {"id":1,"name":"John"},
        {"id":2,"name":"Sam"}
    ]
}

# normal for loop
for user in response1["users"]:
    if user["id"] == 2:
        print(user)

# using list comprehension
result = [user for user in response1["users"] if user["id"] == 2]
print(result)

# Two APIs return the same users but order may differ. Validate both responses are equal.

resp1 = {
"users":[
        {"id":1,"name":"John"},
        {"id":2,"name":"Sam"}
    ]
}

resp2 = {
"users":[
        {"id":2,"name":"Sam"},
        {"id":1,"name":"John"}
    ]
}

sorted1 = sorted(resp1["users"], key=lambda x: x["id"])
sorted2 = sorted(resp2["users"], key=lambda x: x["id"])

print(sorted1 == sorted2)

# Question: Find total order price.

response3 = {
    "data":{
        "orders":[
        {
            "order_id":101,
            "items":[
                {"name":"Laptop","price":1000},
                {"name":"Mouse","price":20}
            ]
        }]
    }
}

total_price = 0
for order in response3["data"]["orders"]:
    for item in order["items"]:
        total_price += item["price"]

print("Total Price = ", total_price)

total_price = [item["price"] for  order in response3["data"]["orders"] for item in order["items"]]
print(sum(total_price))

# Find Missing Fields in JSON Response: Expected fiels: id, name
response = {
    "users":[
        {"id":1,"name":"John"},
        {"id":2}
    ]
}

required = {"id", "name"}
for user in response["users"]:
    missing = required - set(user.keys())
    if missing:
        print("Missing fields: ", missing)