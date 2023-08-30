from django import template
import math

register = template.Library()

@register.simple_tag
def call_sellprice(prix, rabais):
    if rabais is None or rabais is 0:
        return prix
    sellprice = prix
    sellprice = prix - (prix * rabais/100)
    return math.floor(sellprice)