from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    resumen = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(blank=True,null=True)
    tags = models.ManyToManyField(Tag,null=True)

    class Meta:
        ordering = ['fecha_publicacion']

    def __str__(self):
        return self.titulo

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    





