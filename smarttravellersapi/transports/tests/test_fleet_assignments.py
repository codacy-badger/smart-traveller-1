from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import CustomUser
from transports.models import Route, Fleet, FleetType, FleetAssignment


class FleetAssignmentTests(APITestCase):
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
        self.url_fleet_assign = 'http://127.0.0.1:8000/api/v1/fleet-assignments/'
        self.data_fleet_assign = {
                                'fleet_registration_no': 1,
                                'route_name': 1,
                                'trip_start_date': '2020-02-16 08:00',
                                'trip_end_date': '2020-02-17 09:00',
                                'status': 'True',
                                'created_by': 16
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
        fleet_type = FleetType.objects.create(name="Universal", status="True", created_by=user)
        self.fleet = Fleet.objects.create(registration_no='UAA001D', engine_no='UA000-01317890', chasis_no='AE100-0121000',
                    model_no='AE000', fleet_type=fleet_type, layout='2 - 3', seat_nos=69, status='True', created_by=user)
        self.route = Route.objects.create(name='Route 1', description='The trip from Kampala to Moyo', start_point='Kampala',
                            end_point='Moyo', stopage_points='Adjumani, Kigumba', distance=540,
                            approximate_time='09:00:00', status='True', created_by=user)
        self.fla = {
            'fleet_registration_no': self.fleet.id,
            'route_name': self.route.id,
            'trip_start_date': '2020-02-17 08:00',
            'trip_end_date': '2020-02-18 09:00',
            'status': 'True',
            'created_by': user.id
        }
        self.client.post(self.url_fleet_assign, self.fla, format='json')

    def test_fleet_assign_can_be_created(self):
        """
        Ensure we can create a new fleet assignment.
        """
        self.auth_user()
        response = self.client.post(self.url_fleet_assign, self.data_fleet_assign, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['fleet_registration_no'], 1)
        self.assertEqual(FleetAssignment.objects.count(), 2)

    def test_fleet_assign_can_be_retrieved(self):
        """
        Ensure we can retrieve a fleet assignment.
        """
        self.auth_user()
        resp = self.client.get(self.url_fleet_assign)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)

    def test_fleet_assign_can_be_updated(self):
        """
        Ensure we can update a fleet assign.
        """
        self.auth_user()
        data = {'trip_start_date': '2020-02-16 08:30', 'trip_end_date': '2020-02-17 09:30' }
        url = 'http://127.0.0.1:8000/api/v1/fleet-assignments/5/'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['id'], 5)

    def test_fleet_assign_can_be_deleted(self):
        """
        Ensure we can delete a fleet assign.
        """
        self.auth_user()
        url = 'http://127.0.0.1:8000/api/v1/fleet-assignments/3/'
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FleetAssignment.objects.count(), 0)
