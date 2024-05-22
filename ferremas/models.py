from django.db import models

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombreart = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, default='Sin marca')
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.nombreart