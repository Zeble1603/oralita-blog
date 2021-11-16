from django.shortcuts import render
from translations.es.messages import Default, Donde, Especialidades, Homepage,Horario,Form,Global, PrimeraVisita, QuienesSomos



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
    return render(request, 'base.html', context=context)

def quien(request):
    return render(request, 'quienes_somos.html', context={'quienes_somos': QuienesSomos,})



