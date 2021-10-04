# __init__.py file ensures that cart_tools.py is treated as Python package
# This allows cart_tools module to be available for imports and use in templates

from django import template


register = template.Library()

# decorator to register function as template filter
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity