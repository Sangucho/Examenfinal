from django.db import models

# Create your models here.
class Producto(models.Model):
    nombreart = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.nombreart