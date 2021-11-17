from django.shortcuts import render

from translations.es.messages import *
from translations.es.especialidades import *


# Create your views here.

def homeview(request):
    
    context = {
        'default':Default,
        'horario': Horario,
        'form':Form,
        'global':Global,
        'homepage':Homepage,
        'especialidades':Especialidades,
        'quienes_somos': QuienesSomos,
        'donde':Donde,
        'primera_visita':PrimeraVisita,  
        'horario':Horario,  
    }
    return render(request, 'home.html', context=context)

def especialidades(request):
    context ={
        'especialidade':Especialidades,
        'global':Global,
    }
    return render(request, 'especialidades.html', context=context)

def quien(request):
    return render(request, 'quienes_somos.html', context={'quienes_somos': QuienesSomos,})


def donde(request):
    context = {
        'donde':Donde,
        'global':Global,
    }
    return render(request, 'donde.html', context=context)
