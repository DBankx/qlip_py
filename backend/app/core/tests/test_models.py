from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

class TestModels(TestCase):
	"""Test database models"""

	def setUp(self):
		self.test_email = 'test@test.com'
		self.test_password = 'Pa$$w0rd'
		self.first_name = 'Test'
		self.last_name = 'User'
		self.username = 'testuser'

	def test_create_user_with_email_successful(self):
		"""Test that creating user with valid email is successful"""

		user = get_user_model().objects.create_user(email=self.test_email, password=self.test_password, first_name=self.first_name, last_name=self.last_name, username=self.username)

		self.assertEqual(user.email, self.test_email)

		self.assertNotEqual(user.avatar, None);

		self.assertTrue(user.check_password(self.test_password))