from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from translations.es.messages import *
from translations.es.especialidades import *


register = template.Library()

@register.simple_tag
def gen_espe():
    
    special = {

        Odontologia.title : "{% url index:odontologia %}",
        Implantologia.title: "{% url index:implantologia %}",
        Ortodoncia.title: "{% url index:ortodoncia %}",
        Odontopediatria.title: "{% url index:odontopediatria %}",
        Protesis.title: "{% url index:protesis %}",

    }

    html_chunk = ""
    for key,val in special.items():
        html_chunk += format_html("<li><a href='{}'>{}</a></li>",mark_safe(val),mark_safe(key))

    return mark_safe(html_chunk)