from django.contrib import admin
from django.db import models

# Create your models here.

class Especialidad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='especialidades')
    description = models.TextField(max_length=200)
    alt_img = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Especialidades"
    

class EspeModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
