import requests

def test_create_user_with_nested_data():
    payload = {
        "user": {
            "name": "Atharva",
            "email": "atharva@test.com"
        },
        "address": {
            "city": "Nagpur",
            "zip": "440001"
        }
    }

    url = "https://api.example.com/users"

    headers = {
        "Authorization": "Bearer TOKEN",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.status_code)
    print(response.json())

    data = response.json()

    # assertion
    expected_status_code = 201
    actual_stats_code = response.status_code
    assert actual_stats_code == expected_status_code

    assert data["user"]["name"] == "Atharva"
    assert data["address"]["city"] == "Nagpur"

