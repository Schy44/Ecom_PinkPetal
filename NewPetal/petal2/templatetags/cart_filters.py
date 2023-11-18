from django import template

register = template.Library()


@register.filter
def total_price(cart_items):
    total = sum(item.price * item.quantity for item in cart_items)
    return total
