from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python

class ClientManager(BaseUserManager):

    def create_user(self, first_name=None, last_name=None, birth_day=None, email=None, password=None, phone=None, country=None, residence_location=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            birth_day=birth_day,
            email=email,
            phone=to_python(phone),
            country=country,
            residence_location=residence_location,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            username=username,
            email=email,
            password=password,
            **kwargs
        )

class Client(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True, default='', null=True)
    last_name = models.CharField(max_length=150, blank=True, default='', null=True)
    birth_day = models.DateField(null=True)
    phone = PhoneNumberField(blank=True, null=True)
    country = models.CharField(max_length=100, null=True)
    residence_location = models.CharField(max_length=200, null=True)
    objects = ClientManager()

    def __str__(self):
        return self.first_name or self.username

