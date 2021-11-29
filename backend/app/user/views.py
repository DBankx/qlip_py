from rest_framework import authentication, permissions, generics
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializer

class RegisterUserView(generics.CreateAPIView):
	"""Create a new user in the system"""
	serializer_class = serializer.RegisterSerializer		

class LoginUserView(ObtainAuthToken):
	"""Handle user authentication"""
	serializer_class = serializer.LoginSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
	"""Manage authenticated user"""	
	pass