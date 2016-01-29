from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter(name='is_form_set')
def is_form_set_tag(obj):
    return hasattr(obj, 'initial_form_count')

@register.filter(name='get_absolute_uri')
def get_absolute_uri(request, resume):
    location = reverse("display_resume", kwargs={'access_url':resume.access_url})
    return request.build_absolute_uri(location)
