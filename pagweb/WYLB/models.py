from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Usuario(models.Model):
    nombres = models.CharField(max_length=20),
    apellido= models.CharField(max_length=20),
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True),
    password = models.CharField(max_length=30)


    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            str(self.nombres)
            + " "
            + str(self.apellido)
        )

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    rutaImg1 = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return (
            "nombre: " +
            str(self.nombre)
            + ", precio: $"
            + str(self.precio)
        )