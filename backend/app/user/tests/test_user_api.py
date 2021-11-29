from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

REGISTER_URL = reverse('user:register')
LOGIN_URL = reverse('user:login')

def create_sample_user(**data):
	"""Create a new sample user with data"""
	return get_user_model().objects.create_user(**data)

		 

class PublicUserApiTests(TestCase):
	"""Testing the public user api"""

	def setUp(self):
		self.client = APIClient();

	def test_register_successful_with_valid_data(self):
		"""Test register returns 201"""

		payload = {
			'email': 'test@test.com',
			'username': 'testman',
			'first_name': 'test',
			'last_name': 'man',
			'password': 'testpass'
		}

		res = self.client.post(REGISTER_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_201_CREATED)

		user = get_user_model().objects.get(**res.data)

		self.assertEqual(user.username, payload['username'])

		self.assertEqual(user.password, payload['password'])

	def test_register_unsuccessful_with_invalid_data(self):
		"""Test register with invalid data returns 400"""

		payload = {
			'email': ''
		}

		res = self.client.post(REGISTER_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

	def test_login_successful(self):
		"""Test login returns token on successful login"""

		create_sample_user(username='testman', password='Pa$$w0rd', email='test@test.com', first_name='test', last_name='man')

		payload = {
			'email': 'test@test.com',
			'password': 'Pa$$w0rd'
		}

		res = self.client.post(LOGIN_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_200_OK)

		self.assertIn('token', res.data)

	def test_login_unsuccessful_with_invalid_data(self):
		"""Test login returns 400 on unsuccessful login"""

		create_sample_user(username='testman', password='Pa$$w0rd', email='test@test.com', first_name='test', last_name='man')

		payload = {
			'email': 'testman@test.com',
			'password': 'Cigrig'
		}

		res = self.client.post(LOGIN_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

		self.assertNotIn('token', res.data)
		
