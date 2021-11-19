from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

class TestModels(TestCase):
	"""Test database models"""

	def setUp(self):
		self.test_email = 'test@test.com'
		self.test_password = 'Pa$$w0rd'

	def test_create_user_with_email_successful(self):
		"""Test that creating user with valid email is successful"""

		user = get_user_model().objects.create_user(email=self.test_email, password=self.test_password)

		self.assertEqual(user.email, self.test_email)

		self.assertTrue(user.check_password(self.test_password))