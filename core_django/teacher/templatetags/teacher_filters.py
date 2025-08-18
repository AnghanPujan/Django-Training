from django import template

register = template.Library()

@register.filter
def capitalize_words(value):
    return value.title() if isinstance(value, str) else value

@register.filter    
def mask_email(value):
    try:
        username, domain = value.split("@")
        return username[:3] + "*****@" + domain
    except:
        return value
