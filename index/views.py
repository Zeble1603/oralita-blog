import importlib
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.utils.translation import get_language
from .models import Especialidad
from translations.es.messages import *
from translations.es.especialidades import *
import environ

from mailjet_rest import Client



# ================================================= 
# Context used in the different views for index app
# =================================================

index_context = {

        'default':Default,
        'horario': Horario,
        'form':Form,
        'global':Global,
        'homepage':Homepage,
        'especialidades':Especialidades,
        'quienes_somos': QuienesSomos,
        'donde':Donde,
        'primera':PrimeraVisita,
        'horario':Horario,  
        'contact':Contact,
        'thanks': Thanks,
        'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
    }

# ================
# Custom functions 
# ================

# Convert a string into an object 
def class_by_name(module_name, class_name):
    # load the module
    module = __import__(module_name, globals(), locals(), class_name)
    # get the class
    c = getattr(module, class_name)
    return c



# ===========
# Index views 
# ===========

class EspecialidadDetailView(DetailView):
    model = Especialidad
    template_name = "especialidades.html"
    extra_context = index_context

class EspecialidadesListView(ListView):
    model = Especialidad
    template_name = "especialidades_list.html"
    extra_context = index_context

def homeview(request):
    home_context = {
        'especialidad' : Especialidad,
        'especialidad_list' : Especialidad.objects.order_by('id')
    }
    index_context.update(home_context)
    return render(request, 'home.html', context=index_context)


def especialidades(request):
    return render(request, 'especialidades_list.html', context=index_context)

def especialidad_detail(request,name):
    especialidad = class_by_name('translations.es.especialidades',name)
    especialidad_context = {
        'especialidad' : especialidad,
    }
    especialidad_context.update(index_context)
    return render(request, 'especialidades.html', context=especialidad_context)

def quien(request):
    home_context = {
        'especialidad' : Especialidad,
        'especialidad_list' : Especialidad.objects.all()
    }
    index_context.update(home_context)
    return render(request, 'quienes_somos.html', context=index_context)


def donde(request):
    home_context = {
        'especialidad' : Especialidad,
        'especialidad_list' : Especialidad.objects.all()
    }
    index_context.update(home_context)
    return render(request, 'donde.html', context=index_context)


def primera(request):
    home_context = {
        'especialidad' : Especialidad,
        'especialidad_list' : Especialidad.objects.all()
    }
    index_context.update(home_context)
    return render(request, 'primera_visita.html', context=index_context)


def contact(request):
    home_context = {
        'especialidad' : Especialidad,
        'especialidad_list' : Especialidad.objects.all()
    }
    index_context.update(home_context)
    return render(request, 'form/contact.html', context=index_context)



#Form correctly filled, send email. 

def contact_submit(request):
    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env('MJ_APIKEY_PUBLIC')
    API_SECRET = env('MJ_APIKEY_PRIVATE')

    mailjet = Client(auth=(API_KEY, API_SECRET),version='v3.1')

    message = """
    Solicitud de cita
    Locale : {}
    Desde: {}
    Teléfone: {}
    E-mail: {}
    Fecha: {} {}
    Mensaje: {}
    """.format(
        get_language(),
        request.POST['name'],
        request.POST['phone'],
        request.POST['email'],
        request.POST['date'], request.POST['time'],
        request.POST['message'],
    )

    data = {
                'Messages': [   
                    {
                    "From": {
                        "Email": "info@oralita.com",
                        "Name": "Oralita.com"
                    },
                    "To": [
                        {
                        "Email": "info@oralita.com",
                        "Name": "You"
                        }
                    ],
                    "Subject": "Solicitud de cita!",
                    "TextPart": message,
                    }
                ]
            }

    result = mailjet.send.create(data=data)
    print(API_KEY,API_SECRET,result.status_code)

    return HttpResponse("""<div class="message message-close message-success">
			<button type="button" class="message-close-button"><i class="fa fa-close"></i></button>
			<div class="alert alert-success">Votre message a été envoyé</div>
		    </div>""") 
    
