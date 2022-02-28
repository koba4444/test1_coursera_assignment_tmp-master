from django import template

register = template.Library()

@register.filter
def sum(a, b):
    print(int(a) + int(b))
    pass

@register.filter
def inc(a, b):
    return str(int(a) + (b))
