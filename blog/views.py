from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .models import *

# Create your views here.

class PostListView(ListView):
    model = Articulo
    template_name = "list.html"

class PostDetailView(DetailView):
    model = Articulo
    template_name = "detail.html"