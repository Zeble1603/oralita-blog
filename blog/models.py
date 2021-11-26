from django.contrib import admin
from django.db import models
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class Tag(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    photo = models.ImageField(blank=True,null=True,upload_to="images")
    texto = RichTextUploadingField(blank=True, null=True)
    resumen = models.TextField(max_length=500)
    fecha = models.DateField(blank=True,null=True)
    tags = models.ManyToManyField(Tag,blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def publicar(self):
        self.publicado = True
        self.fecha = timezone.now()
        self.save()
        

    





