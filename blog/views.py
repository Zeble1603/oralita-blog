from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from django.utils import timezone

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
        return context

def articulos_filtrados(request,slug):
    tag = Tag.objects.get(slug=slug)
    categoria = tag.nombre
    articulos_categoria = Articulo.objects.filter(fecha__lte=timezone.now(),tags__nombre=categoria)
    context = {
        'articulos_categoria':articulos_categoria,
        'categoria':categoria
    }
    context.update(index_context)
    return render(request,'categorias.html',context=context)

class PostDetailView(DetailView):
    model = Articulo
    template_name = "articulo_detail.html"
    extra_context = index_context