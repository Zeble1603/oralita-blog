from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from translations.es.messages import *
from translations.es.especialidades import *


register = template.Library()

@register.simple_tag
def gen_espe():
    
    special = {

        Odontologia.title : Odontologia.link,
        Implantologia.title: Implantologia.link,
        Ortodoncia.title: Ortodoncia.link,
        Odontopediatria.title: Odontopediatria.link,
        Protesis.title: Protesis.link,

    }

    html_chunk = ""
    for key,val in special.items():
        html_chunk += format_html("<li><a href='{% url 'index:especialidad_detail' name={} %}'>{}</a></li>",mark_safe(val),mark_safe(key))

    return mark_safe(html_chunk)