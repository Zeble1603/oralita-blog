from django.contrib import admin
from django.db import models
from django.db.models import ManyToManyField
from django.db.models.signals import pre_save
from django.forms import CheckboxSelectMultiple
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


# Models used on this app

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=300)
    photo = models.ImageField(upload_to="images")    

    def __str__(self):
        return "{} {} ".format(self.nombre,self.apellido)

    class Meta:
        verbose_name_plural = "Autores"    



class Tag(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("blog:categoria", kwargs={"slug": self.slug})
        

class TagModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}



class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    meta_titulo = models.CharField(max_length=60,blank=True,null=True)
    photo = models.ImageField(blank=True,null=True,upload_to="images")
    resumen = models.TextField(max_length=200)
    meta_description = models.CharField(max_length=155,blank=True,null=True)
    texto = RichTextUploadingField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True,null=True)
    tags = models.ManyToManyField(Tag,blank=True)
    publicado = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
        

        
class ArticuloModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    prepopulated_fields = {"slug": ("titulo",)}


