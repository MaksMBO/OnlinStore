from django import template

register = template.Library()

@register.filter(name='sum_price')
def sum_price(value):
    total_price = 0
    for product in value:
        total_price += product.price 
        
    return total_price