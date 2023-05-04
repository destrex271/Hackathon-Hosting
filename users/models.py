from enum import unique
from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser):
    email                   = models.EmailField(unique=True)
    is_organizer            = models.BooleanField(default=False)
    dob                     = models.DateField()
    organization            = models.CharField()

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

