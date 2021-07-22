import requests

def client():

    # data = {
    #     "username" : "resttest",
    #     "email" : "test@rest.com",
    #     "password1" : "testtest0000",
    #     "password2" : "testtest0000",
    # }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration", data=data)

    token_h = "Token 57baa8d4906107dff3b9ad022e847865d7e00218"
    headers = {"Authorization" : token_h}
    
    response = requests.get("http://127.0.0.1:8000/api/publics/", headers=headers)
    
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()