import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework                  import response, status
from rest_framework.authtoken.models import Token
from rest_framework.test             import APITestCase
from api.publics.models import Public

class PublicTestCase(APITestCase):
    def setUp(self):
        Public.objects.create(id=1, name="한성봉", password='1234', household_number='2001', payment=1000)

    def test_public_list_success(self):
        data = {'password':'1234', 'household_number':'2001'}

        response = self.client.post('/api/publics/', data =json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id':1, 'name':'한성봉', 'password':'1234', 'household_number':'2001', 'payment':'1000.000'})

    def test_public_list_bad_request(self):
        data = {'password':'1230', 'household_number':'2002'}

        response = self.client.post('/api/publics/', data =json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'MESSAGE' : '입력하신 정보와 일치하지 않습니다.'})
