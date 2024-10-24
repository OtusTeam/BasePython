from django import template

register = template.Library()


@register.filter(name='upper_name')
def upper_name(value):
    return value.upper()