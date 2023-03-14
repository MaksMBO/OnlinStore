from django.db import models
from django.urls import reverse

class ProductsImg(models.Model):
    img = models.FileField(upload_to='uploads/', verbose_name = 'Зображення')
    
    class Meta: 
        verbose_name = 'Зображення товару'
        verbose_name_plural = 'Зображення товару'
        
    def __str__(self):
       return self.img.url


class ProductsType(models.Model):
    type = models.CharField(max_length=200, default=None, verbose_name = 'Типи товару')
    
    class Meta: 
        verbose_name = 'Типи товару'
        verbose_name_plural = 'Типи товару'
        
    
    def __str__(self):
        return self.type


class ProductsBrand(models.Model):
    brand = models.CharField(max_length=200, default=None, verbose_name = 'Бренди')
    
    class Meta: 
        verbose_name = 'Бренди'
        verbose_name_plural = 'Бренди'
    
    def __str__(self):
        return self.brand


class Products(models.Model):
    title = models.CharField(max_length=200, default=None, verbose_name = 'Назва')
    price =  models.DecimalField(max_digits=10, decimal_places=0, verbose_name = 'Ціна')
    img = models.ManyToManyField(ProductsImg, verbose_name = 'Зображення')
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE, verbose_name = 'Тип товару')
    brand = models.ForeignKey(ProductsBrand, on_delete=models.CASCADE, verbose_name = 'Бренд')
    is_available = models.BooleanField(default=False, verbose_name = 'Наявність')
    
    class Meta: 
        verbose_name = 'Товари'
        verbose_name_plural = 'Товари'
    
    def get_pk(self):
        return reverse('aboutProduct', kwargs={'id': self.pk})
    
    def aboutProduct(self, id):
        return reverse('aboutProduct', kwargs={'id': self.pk})
    
    def __str__(self):
        return self.title
