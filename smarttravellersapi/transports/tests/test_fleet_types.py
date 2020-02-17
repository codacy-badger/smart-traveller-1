from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import CustomUser
from transports.models import FleetType


class FleetTypeTests(APITestCase):
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
        self.url_fleet_type = 'http://127.0.0.1:8000/api/v1/fleet-types/'
        self.data_fleet_type = {
                                'name': 'Premium',
                                'status': 'True',
                                'created_by': 20
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
        FleetType.objects.create(name="Universal", status="True", created_by=user)

    def test_create_fleet_type(self):
        """
        Ensure we can create a new fleet type.
        """
        self.auth_user()
        response = self.client.post(self.url_fleet_type, self.data_fleet_type, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Premium')
        self.assertEqual(FleetType.objects.count(), 2)

    def test_retrieve_account(self):
        """
        Ensure we can retrieve a fleet type.
        """
        self.auth_user()
        resp = self.client.get(self.url_fleet_type)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)

    def test_fleet_type_can_be_updated(self):
        """
        Ensure we can update a fleet type.
        """
        self.auth_user()
        data = {'name': 'Day Premium'}
        url = 'http://127.0.0.1:8000/api/v1/fleet-types/8/'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['name'], 'Day Premium')

    def test_fleet_type_can_be_deleted(self):
        """
        Ensure we can delete a fleet type.
        """
        self.auth_user()
        url = 'http://127.0.0.1:8000/api/v1/fleet-types/7/'
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FleetType.objects.count(), 0)
