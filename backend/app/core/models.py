from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class UserManager(BaseUserManager):
	"""User manager for the user db model"""
	
	def create_user(self, email, username, first_name, last_name, password, **extra_fields):
		"""Create and return new user with all valid input"""

		if not email or not username or not first_name or not last_name or not password:
			raise ValueError('All fields are required')

		user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, avatar=f'https://ui-avatars.com/api/?name={first_name}+{last_name}', **extra_fields)

		user.set_password(password)

		user.save(using=self._db)

		return user

	def create_superuser(self, email, username, first_name, last_name, password):

		user = self.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password)

		user.is_superuser = True

		user.is_staff = True

		user.save(using=self._db)

		return user

class User(AbstractBaseUser, PermissionsMixin):
	"""Db model for application user"""

	first_name = models.CharField(max_length=225)

	last_name = models.CharField(max_length=225)

	username_validation = RegexValidator(regex=r"^(?=.{4,32}$)(?![.-])(?!.*[.]{2})[a-zA-Z0-9.-]+(?<![.])$", message="Username format is invalid")
	username = models.CharField(max_length=32, unique=True, validators=[username_validation], blank=False, null=False)

	bio = models.TextField(blank=True)

	country = CountryField()

	avatar = models.CharField(max_length=225, blank=False, null=False)

	email = models.EmailField(unique=True, blank=False, null=False, max_length=225)

	# ADMIN PROPERTIES
	is_staff = models.BooleanField(default=False)

	is_active = models.BooleanField(default=True)

	# SYSTEM PROPERTIES
	has_on_boarded = models.BooleanField(default=False)

	is_email_verified = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'