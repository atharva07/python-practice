import requests

url = "https://example.com/upload"

headers = {
    "Authorization": "Bearer TOKEN"
}

file = {
    "file": open("test.pdf", "rb")
}

response = requests.post(url, headers=headers, files=file)

assert response.status_code == 200, f"Expected 200 but {response.status_code}"
print(response.json())


