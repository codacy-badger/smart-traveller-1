from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import Agent, CustomUser

class AgentTests(APITestCase):
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
        self.url_agent = 'http://127.0.0.1:8000/api/v1/agents/'
        self.data_agent = {'mobile': '+256744444444',
                    'username': 'agent',
                    'email':'agent@smart.com',
                    'first_name': 'agent',
                    'last_name': 'first',
                    'password':'0agent0',
                    'station': 'wakiso',
                    'present_address': 'mukono',
                    'permanent_address': 'karuma town council',
            }
        self.url2 = 'http://127.0.0.1:8000/api/v1/auth/login/'
        self.data2 = {'username': 'testme', 'email':'test@test.com', 'password': 'testme2020'}

    def auth_user(self):
        self.client.post(self.url, self.data, format='json')
        self.client.post(self.url2, self.data2, format='json')
        user = CustomUser.objects.get(username='testme')
        user.is_staff = True
        return user

    def test_create_agent_account(self):
        """
        Ensure we can create a new agent account.
        """

        user = self.auth_user()
        user.save()
        response = self.client.post(self.url_agent, self.data_agent, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agent.objects.get().username, 'agent')
        self.assertEqual(Agent.objects.get().mobile, '+256744444444')

    def test_agent_can_login(self):
        """
        Ensure an agent can login to their account.
        """
        self.url2_agent = 'http://127.0.0.1:8000/api/v1/auth/login/'
        self.data2_agent = {'username':'agent', 'email':'agent@smart.com', 'password':'0agent0'}
        user = self.auth_user()
        user.save()
        self.client.post(self.url_agent, self.data_agent, format='json')
        self.client.logout()
        resp = self.client.post(self.url2_agent, self.data2_agent, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_agent_account_can_be_update(self):
        """
        Ensure we can update an agent account.
        """

        user = self.auth_user()
        user.is_admin = True
        user.save()
        self.client.post(self.url_agent, self.data_agent, format='json')
        data = {'mobile': '+256755555555',
                'username': 'agent9',
                'email':'agent@smart.com',
                'first_name': 'agent9',
                'last_name': 'first',
                'password':'0agent0',
                'station': 'kampala',
                'present_address': 'ntinda',
                'permanent_address': 'gulu city',
            }
        url = 'http://127.0.0.1:8000/api/v1/agents/4/'
        resp = self.client.patch(url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_agent_account_can_be_deleted(self):
        """
        Ensure we can delete an agent account.
        """

        user = self.auth_user()
        self.client.post(self.url_agent, self.data_agent, format='json')
        user.is_admin = True
        user.save()
        link = 'http://127.0.0.1:8000/api/v1/agents/2/'
        resp = self.client.delete(link)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agent.objects.count(), 0)

    def test_retrieve_account(self):
        """
        Ensure we can retrieve agent account.
        """

        user = self.auth_user()
        self.client.post(self.url_agent, self.data_agent, format='json')
        user.save()
        link = 'http://127.0.0.1:8000/api/v1/agents/'
        resp = self.client.get(link)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)
