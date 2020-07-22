from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status


class ConvertionTest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('convert')

    def test_convertion_with_input(self):
        data = {
            'from_currency': 'USD', 
            'to_currency': 'NGN', 
            'amount': 10
        }
        response = self.client.post(self.url, data=data, format='json')
        print('Response status code: ' + str(response.status_code))

        self.assertEquals(response.status_code, 200)

    def test_convertion_without_inputs(self):
        response = self.client.post(path='/convert_currency/')
        print('Response status code: ' + str(response.status_code))

        self.assertEqual(response.status_code, 404)
