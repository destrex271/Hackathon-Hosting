from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser):
    first_name              = models.CharField(max_length=100)
    last_name              = models.CharField(max_length=100)
    email                   = models.EmailField(unique=True)
    is_organizer            = models.BooleanField(default=False)
    dob                     = models.DateField()
    organization            = models.CharField()

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

