from django.contrib import admin
from django.utils.safestring import mark_safe

from catalog.models import Products, ProductsBrand, ProductsType, ProductsImg


class ProductsImgAdmin(admin.ModelAdmin):
    list_display = ('get_img', )
    fields = ('img', 'get_img', )
    readonly_fields = ('get_img', )
    
    def get_img(self, obj):
        return mark_safe(f"<div class='div_img_admin'> <img src='/{obj.img}' class='img_admin'> </div>")
    
    get_img.short_description = 'Зображення'


class ProductsTypeAdmin(admin.ModelAdmin):
    list_display = ('type', )
    list_display_links = ('type', )
    search_fields = ('type', )


class ProductsBrandAdmin(admin.ModelAdmin):
    list_display = ('brand', )
    list_display_links = ('brand', )
    search_fields = ('brand', )


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_img', 'is_available')
    list_display_links = ('title', )
    list_editable = ['is_available']
    search_fields = ('title', )
    fields = ('title', 'price', 'is_available', 'img', 'get_img')
    readonly_fields = ('get_img', )
    filter_horizontal = ('img',)
    
    def get_img(self, obj):
        context = ''
        for p in obj.img.all():
            context += f"<div class='div_img_admin'> <img src='{p.img.url}' class='img_admin'> </div>"
        return mark_safe(context)
    
    get_img.short_description = 'Зображення'

admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsBrand, ProductsBrandAdmin)
admin.site.register(ProductsType, ProductsTypeAdmin)
admin.site.register(ProductsImg, ProductsImgAdmin)
