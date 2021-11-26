from django.contrib import admin
from django.contrib.auth.models import Group

from . import models

# Register your models here.

admin.site.site_header = 'Administración del Blog de Oralita'

admin.site.register(models.Articulo,models.ArticuloModelAdmin)
admin.site.register(models.Autor)
admin.site.register(models.Tag,models.TagModelAdmin)
admin.site.unregister(Group)