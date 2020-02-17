from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import CustomUser
from transports.models import Route


class RouteTests(APITestCase):
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
        self.url_route = 'http://127.0.0.1:8000/api/v1/routes/'
        self.data_route = {
                                'name': 'Route 2',
                                'description': 'The trip from Moyo to Kampala',
                                'start_point': 'Moyo',
                                'end_point': 'Kampala',
                                'stopage_points': 'Kigumba, Adjumani',
                                'distance': 540.0,
                                'approximate_time': '09:00:00',
                                'status': 'True',
                                'created_by': 32
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
        Route.objects.create(name='Route 1', description='The trip from Kampala to Moyo', start_point='Kampala',
                            end_point='Moyo', stopage_points='Adjumani, Kigumba', distance=540,
                            approximate_time='09:00:00', status='True', created_by=user)

    def test_route_can_be_created(self):
        """
        Ensure we can create a new route.
        """
        self.auth_user()
        response = self.client.post(self.url_route, self.data_route, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Route 2')
        self.assertEqual(Route.objects.count(), 2)

    def test_route_can_be_retrieved(self):
        """
        Ensure we can retrieve a route.
        """
        self.auth_user()
        resp = self.client.get(self.url_route)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)

    def test_route_can_be_updated(self):
        """
        Ensure we can update a route.
        """
        self.auth_user()
        data = {'name': 'Route 3'}
        url = 'http://127.0.0.1:8000/api/v1/routes/9/'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['name'], 'Route 3')

    def test_route_can_be_deleted(self):
        """
        Ensure we can delete a route.
        """
        self.auth_user()
        url = 'http://127.0.0.1:8000/api/v1/routes/7/'
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Route.objects.count(), 0)
