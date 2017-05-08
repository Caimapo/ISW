from django.db import models
#from djangotoolbox.fields import ListField

# Create your models here.
class Documento(models.Model):
    texto = models.CharField(max_length=10000)
    def __str__(self):
        return self.texto

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
class Document(models.Model):
    texto = models.CharField(max_length=20000)
    numero = models.IntegerField()
    #urllist = ListField()
    def __str__(self):
        return self.numero