from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from django.utils import timezone
from index.models import Especialidad

from .models import *
from index.views import index_context
# Create your views here.

class PostListView(ListView):
    model = Articulo
    template_name = "articulos.html"    
    extra_context = index_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulo_list'] = Articulo.objects.filter(fecha__lte=timezone.now())
        context['tag_list'] = Tag.objects.all()
        context['especialidad'] = Especialidad
        context['especialidad_list'] = Especialidad.objects.all()
        return context

def articulos_filtrados(request,slug):
    tag = Tag.objects.get(slug=slug)
    tag_list = Tag.objects.all()
    categoria = tag.nombre
    articulo_list = Articulo.objects.filter(fecha__lte=timezone.now(),tags__nombre=categoria)
    context = {
        'articulo_list':articulo_list,
        'categoria':categoria,
        'tag_list' : tag_list,
        'tag':tag,
    }
    context.update(index_context)
    return render(request,'articulos.html',context=context)

class PostDetailView(DetailView):
    model = Articulo
    template_name = "articulo_detail.html"
    extra_context = index_context