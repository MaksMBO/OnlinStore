from django.contrib import admin

from catalog.models import Products, ProductsBrand, ProductsType, ProductsImg

admin.site.register(Products)
admin.site.register(ProductsBrand)
admin.site.register(ProductsType)
admin.site.register(ProductsImg)
