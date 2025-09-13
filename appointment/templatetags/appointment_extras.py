from django import template
register = template.Library()

@register.filter
def dict_get(d, key):
    return d.get(key)
    
@register.filter
def index(List, i):
    try:
        return List[i-1]
    except:
        return ''
