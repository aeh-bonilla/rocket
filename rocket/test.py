from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

class RocketTest(APITestCase):

    def test_add_task(self):

        client = APIClient()
        response=client.post('/api/add_task/', {'description': 'test 2',
                'duration':'1'})


        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):

        client = APIClient()
        response=client.post('/api/update_task/', {'id': 1,'description':'modificacion',
                'duration':72,'registered':90,'status':'pendiente'})


        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        client = APIClient()
        response=client.post('/api/delete_task/', {'id': '1'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)