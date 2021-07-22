import requests

def client():
    # credentials = {"username" : "ssaboo", "password" : "9090"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    token_h = "Token 7119f7b89c63cb45dd7d5ea412459509edfde655"
    headers = {"Authorization" : token_h}

    response = requests.get("http://127.0.0.1:8000/api/admins/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()