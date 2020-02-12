from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import CustomUser

class CustomUserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = 'http://127.0.0.1:8000/api/v1/users/'
        self.data = {'username':'testme',
	            'mobile':'+256799999999',
	            'email':'test@test.com',
                'is_staff': True,
	            'first_name':'test',
	            'last_name':'me',
	            'password':'testme2020'
            }
        self.url2 = 'http://127.0.0.1:8000/api/v1/auth/login/'
        self.data2 = {'username': 'testme', 'email':'test@test.com', 'password': 'testme2020'}

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.get().username, 'testme')
        self.assertEqual(CustomUser.objects.get().mobile, '+256799999999')

    def test_account_login(self):
        """
        Ensure we can login an account.
        """

        self.client.post(self.url, self.data, format='json')
        resp = self.client.post(self.url2, self.data2, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_update_account(self):
        """
        Ensure we can update a new account object.
        """

        self.client.post(self.url, self.data, format='json')
        self.client.post(self.url2, self.data2, format='json')
        data = {'username':'tests',
	            'mobile':'+256799999998',
	            'email':'test@test.com',
	            'first_name':'test',
	            'last_name':'metest',
	            'password':'testme2020'
            }
        url = 'http://127.0.0.1:8000/api/v1/users/5/'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_delete_account(self):
        """
        Ensure we can delete an account object.
        """

        self.client.post(self.url, self.data, format='json')
        self.client.post(self.url2, self.data2, format='json')
        link = 'http://127.0.0.1:8000/api/v1/users/3/'
        resp = self.client.delete(link)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_retrieve_account(self):
        """
        Ensure we can list account objects.
        """

        self.client.post(self.url, self.data, format='json')
        self.client.post(self.url2, self.data2, format='json')
        link = 'http://127.0.0.1:8000/api/v1/users/'
        resp = self.client.get(link)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)
