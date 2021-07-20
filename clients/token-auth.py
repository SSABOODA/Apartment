import requests

def client():
    
    credentials = {"username" : "ssaboo", "password" : "tk043528qn"}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    # headers = {"Authorization" : token_h}
    # token_h = "Token 7d6ee5550944e34a66fd5265c83645e375183bec"

    # response = requests.get("http://127.0.0.1:8000/api/admins/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()