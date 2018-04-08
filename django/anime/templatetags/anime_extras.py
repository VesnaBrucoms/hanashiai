from django import template

register = template.Library()


@register.filter
def get_index(value, arg):
    try:
        return value[arg]
    except:
        return None
