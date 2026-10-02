import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Test",
    "body": "Automation",
    "userId": 1
}   

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
actual_status_code = response.status_code
data = response.json()

assert actual_status_code == 201
actual_body = data["body"]
assert actual_body == "Automation"

print("-------------- Authentication ------------------")

headers = {
    "Authorization": "Bearer TOKEN",
    "headers": "application/json"
}

response = requests.get(url, headers=headers)

status_code = response.status_code
data = response.json()

assert status_code == 200
user_id = data["id"]
assert user_id == 10101