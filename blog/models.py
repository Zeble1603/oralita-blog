from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    resumen = models.CharField(max_length=200)
    fecha = models.DateField(blank=True,null=True)
    tags = models.ManyToManyField(Tag,blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def publicar(self):
        self.publicado = True
        self.fecha = timezone.now()
        self.save()
        

    





