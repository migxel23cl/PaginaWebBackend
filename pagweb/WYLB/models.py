from django.db import models

# Create your models here.
 class Usuario(models.Model):
    id = models.AutoField(max_length=5)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()