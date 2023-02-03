from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Class for describing a model with a user"""

    phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return f"{self.username}"
