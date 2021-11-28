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
from django.utils.translation import gettext_lazy as _
from django.urls import path

from . import views


app_name = 'index'

urlpatterns = [
    path('', views.homeview,name='home'),
    path(_('especialidades'),views.EspecialidadesListView.as_view(),name='especialidades'),
    path(_('especialidades/<slug:slug>'),views.EspecialidadDetailView.as_view(),name='especialidad_detail'),
    path(_('quienes-somos'),views.quien,name='quienes-somos'),
    path(_('donde-esta-nuestra-clinica-dental'),views.donde,name='donde'),
    path(_('primera-visita'),views.primera,name='primera_visita'),
    path(_('contacto'),views.contact, name='contact'),
]
