import requests

def test_create_user():
    url = "https://api.example.com/users"

    headers = {
        "Authorization": "Bearer TOKEN",
        "Content-Type": "application/json"
    }

    payload = {
        "name": "Atharva",
        "email": "atharva@test.com"
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()
    status_code = response.status_code

    assert status_code == 201, f"Expected 201 but got {response.status_code}"
    name = data["name"]
    assert name == "Atharva"
    email = data["email"]
    assert email == "atharva@test.com"