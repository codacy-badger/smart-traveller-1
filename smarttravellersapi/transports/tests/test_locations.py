from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import CustomUser
from transports.models import Location


class LocationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = 'http://127.0.0.1:8000/api/v1/users/'
        self.data = {'username':'testme',
	            'mobile':'+256799999999',
	            'email':'test@test.com',
	            'first_name':'test',
	            'last_name':'me',
	            'password':'testme2020'
            }
        self.url_location = 'http://127.0.0.1:8000/api/v1/locations/'
        self.data_location = {
                                'name': 'Kampala',
                                'description': 'The boarding point in kampala',
                                'status': 'True',
                                'created_by': 28
                            }
        self.url2 = 'http://127.0.0.1:8000/api/v1/auth/login/'
        self.data2 = {'username': 'testme', 'email':'test@test.com', 'password': 'testme2020'}

    def auth_user(self):
        self.client.post(self.url, self.data, format='json')
        self.client.post(self.url2, self.data2, format='json')
        user = CustomUser.objects.get(username='testme')
        user.is_staff = True
        user.is_admin = True
        user.save()
        Location.objects.create(name="Moyo", description='This is the boarding point in Moyo',
                                status="True", created_by=user)

    def test_location_can_be_created(self):
        """
        Ensure we can create a new location.
        """
        self.auth_user()
        response = self.client.post(self.url_location, self.data_location, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Kampala')
        self.assertEqual(Location.objects.count(), 2)

    def test_location_can_be_retrieved(self):
        """
        Ensure we can retrieve a location.
        """
        self.auth_user()
        resp = self.client.get(self.url_location)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)

    def test_location_can_be_updated(self):
        """
        Ensure we can update a location.
        """
        self.auth_user()
        data = {'name': 'Gulu', 'description': 'This is the boarding point in gulu.'}
        url = 'http://127.0.0.1:8000/api/v1/locations/5/'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['name'], 'Gulu')

    def test_location_can_be_deleted(self):
        """
        Ensure we can delete a location.
        """
        self.auth_user()
        url = 'http://127.0.0.1:8000/api/v1/locations/3/'
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Location.objects.count(), 0)
