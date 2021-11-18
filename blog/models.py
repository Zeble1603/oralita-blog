from django.db import models

# Create your models here.

class Tag(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    tags = models.ManyToManyField(Tag,null=True)



