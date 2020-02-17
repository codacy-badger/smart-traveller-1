from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import CustomUser
from transports.models import FleetType, Fleet


class FleetTests(APITestCase):
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
        self.client.post(self.url, self.data, format='json')
        self.user = CustomUser.objects.get(username='testme')
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()
        self.fleet_type = FleetType.objects.create(name="Universal", status="True", created_by=self.user)
        self.url_fleet = 'http://127.0.0.1:8000/api/v1/fleets/'
        self.data_fleet = {
                                'registration_no': 'UAC022F',
                                'engine_no': 'UA013-01315490',
                                'chasis_no': 'AE100-0121047',
                                'model_no': 'AE065',
                                'fleet_type': 10,
                                'layout': '2 - 3',
                                'seat_nos': 69,
                                'status': 'True',
                                'created_by': 24
                            }
        self.url2 = 'http://127.0.0.1:8000/api/v1/auth/login/'
        self.data2 = {'username': 'testme', 'email':'test@test.com', 'password': 'testme2020'}

    def auth_user(self):
        self.client.post(self.url2, self.data2, format='json')
        Fleet.objects.create(registration_no='UAA001D', engine_no='UA000-01317890', chasis_no='AE100-0121000',
                    model_no='AE000', fleet_type=self.fleet_type, layout='2 - 3', seat_nos=69, status='True', created_by=self.user)

    def test_create_fleet(self):
        """
        Ensure we can create a new fleet.
        """
        self.auth_user()
        response = self.client.post(self.url_fleet, self.data_fleet, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['registration_no'], 'UAC022F')
        self.assertEqual(Fleet.objects.count(), 2)

    def test_retrieve_account(self):
        """
        Ensure we can retrieve a fleet.
        """
        self.auth_user()
        resp = self.client.get(self.url_fleet)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)

    def test_fleet_can_be_update(self):
        """
        Ensure we can update a fleet.
        """
        self.auth_user()
        data = {'registration_no': 'UBB001X'}
        url = 'http://127.0.0.1:8000/api/v1/fleets/7/'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['registration_no'], 'UBB001X')

    def test_fleet_type_can_be_deleted(self):
        """
        Ensure we can delete a fleet.
        """
        self.auth_user()
        url = 'http://127.0.0.1:8000/api/v1/fleets/8/'
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Fleet.objects.count(), 0)
