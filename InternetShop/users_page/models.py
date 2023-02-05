from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Basket(models.Model):
    basket = models.ManyToManyField('catalog.Products', verbose_name = 'Кошик')
    
    class Meta: 
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошик'


class User(AbstractUser):
    """Class for describing a model with a user"""

    phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name = 'Телефон')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'Кошик')
    like = models.ManyToManyField('catalog.Products', related_name='like', null=True, verbose_name = 'Товари що сподобалися')
    comparison = models.ManyToManyField('catalog.Products', related_name='comparison', null=True, verbose_name = 'Товари для порівняня')

    class Meta:
        db_table = 'user' 
        verbose_name = 'Користувачі'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return f'{self.first_name}'
