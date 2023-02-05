from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Basket(models.Model):
    basket = models.ManyToManyField('catalog.Products')


class User(AbstractUser):
    """Class for describing a model with a user"""

    phone = PhoneNumberField(null=False, blank=False, unique=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, blank=True, null=True)
    like = models.ManyToManyField('catalog.Products', related_name='like', blank=True, null=True)
    comparison = models.ManyToManyField('catalog.Products', related_name='comparison', blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.username}'
