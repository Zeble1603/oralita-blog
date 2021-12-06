from django.contrib import admin
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Especialidad(models.Model):
    title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='especialidades')
    description = models.TextField(max_length=200)
    meta_description = models.TextField(max_length=200,blank=True,null=True)
    alt_img = models.CharField(max_length=200)
    text = RichTextUploadingField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Especialidades"
    

class EspeModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
