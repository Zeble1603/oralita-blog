from django.shortcuts import render

from translations.es.messages import *
from translations.es.especialidades import *

# Context used in the different views for index app

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

    }


# Index views 

def homeview(request):
    return render(request, 'home.html', context=index_context)

def especialidades(request):
    return render(request, 'especialidades.html', context=index_context)

def quien(request):
    return render(request, 'quienes_somos.html', context=index_context)


def donde(request):
    return render(request, 'donde.html', context=index_context)

def primera(request):
    return render(request, 'primera_visita.html', context=index_context)