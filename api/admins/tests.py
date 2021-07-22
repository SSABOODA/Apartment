import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework                  import response, status
from rest_framework.authtoken.models import Token
from rest_framework.test             import APITestCase
from api.publics.models import Public

# class RegistrationTestCase(APITestCase):
#     def test_registration(self):
#         data = {
#             "username"  : "ssabootest",
#             "email"     : "ssaboo99@test.com",
#             "password1" : "1111",
#             "password2" : "1111",
#         }

#         response = self.client.post("/api/rest-auth/registration", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AdminTestCase(APITestCase):
    def setUp(self):
        self.user  = User.objects.create_user(username='ssabootest', password='ssaboo123', is_staff = True)
        self.token = Token.objects.create(user=self.user)

        Public.objects.create(id=1, name="한성봉", password='1234', household_number='2001', payment=1000)
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_public_list_authenticated(self):
        response = self.client.get('/api/admins/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{'id':1, 'name':'한성봉', 'password':'1234', 'household_number':'2001', 'payment':'1000.000'}])
    
    def test_public_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/admins/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
