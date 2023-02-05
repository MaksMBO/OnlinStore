from django.db import models

class ProductsImg(models.Model):
    img = models.FileField(upload_to='uploads/')


class ProductsType(models.Model):
    type = models.CharField(max_length=200, default=None)


class ProductsBrand(models.Model):
    brand = models.CharField(max_length=200, default=None)


class Products(models.Model):
    title = models.CharField(max_length=200, default=None)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ForeignKey(ProductsImg, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductsBrand, on_delete=models.CASCADE)
