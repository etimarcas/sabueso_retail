from django.db import models

# Create your models here.
class item(models.Model):
    item = models.CharField("f001_item",max_length=100)
    descripcion = models.CharField("f001_descripcion",max_length=100)
    cantidad = models.IntegerField("f001_cantidad")
    barras = models.CharField("f001_barras",max_length=100)
    atrb1 = models.CharField("f001_atrb1",max_length=100)
    atrb2 = models.CharField("f001_atrb2",max_length=100)
    habilitado = models.BooleanField("f001_habilitado")
    creacion = models.DateTimeField("f001_creacion")
    actualizacion = models.DateTimeField("f001_actualizacion")

    def __str__(self):
        return self.item