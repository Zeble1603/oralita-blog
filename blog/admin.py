from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'Administración del Blog de Oralita'

admin.site.register(models.Articulo)
admin.site.register(models.Tag)
admin.site.unregister(Group)