import requests

def test_get_user():
    url = "https://api.example.com/users/1"

    headers = {
        "Authorization": "Bearer your_token_here",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    # validate status code
    status_code = response.status_code
    assert status_code == 200

    # validate response body
    body = response.json()
    assert body["id"] == 1
    assert "name" in body