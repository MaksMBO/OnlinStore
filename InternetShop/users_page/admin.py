from django.contrib import admin

from users_page.models import User, Basket


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_superuser')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_editable = ['is_superuser']

    
class BasketAdmin(admin.ModelAdmin):
    list_display = ('get_basket', )
    list_display_links = ('get_basket', )
    
    def get_basket(self, obj):
        return "\n".join([p.basket for p in obj.basket.all()])
    
    get_basket.short_description = 'Кошик'

admin.site.register(User, UserAdmin)
admin.site.register(Basket, BasketAdmin)
