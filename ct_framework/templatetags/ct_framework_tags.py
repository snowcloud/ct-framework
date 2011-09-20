from django.conf import settings
from django import template
from django.utils.translation import ugettext as _

register = template.Library()

@register.filter
def synonym(value):
    v = getattr(settings, 'SYNONYMS', {})
    return _(v.get(value, value))
