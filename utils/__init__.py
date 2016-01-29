import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

import string
import random

def get_random_string(length):

    return ''.join(random.choice(string.ascii_uppercase +
                                 string.digits) for _ in range(length))

def is_form_set(form):
    return hasattr(form, 'initial_form_count')

def render_to_pdf(template_src, context_dict):

    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)

    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
