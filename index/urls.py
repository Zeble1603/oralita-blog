"""Index URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.homeview,name='home'),
    path('especialidades',views.especialidades,name='especialidades'),
    path('especialidades/<str:name>',views.especialidad_detail,name='especialidad_detail'),
    path('quienes-somos',views.quien,name='quienes-somos'),
    path('donde-esta-nuestra-clinica-dental',views.donde,name='donde'),
    path('primera-visita',views.primera,name='primera_visita'),
    path('contacto',views.contact, name='contact'),
    
]
