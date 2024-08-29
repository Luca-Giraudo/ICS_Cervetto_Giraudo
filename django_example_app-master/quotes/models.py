from django.db import models
from localflavor.ar.ar_provinces import PROVINCE_CHOICES

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    perfil_empresa = models.ForeignKey('PerfilEmpresa', on_delete=models.CASCADE, null=True, blank=True)
    perfil_usuario = models.ForeignKey('PerfilUsuario', on_delete=models.CASCADE, null=True, blank=True)
    favoritos = models.ForeignKey('Favorito', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class PerfilEmpresa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=144)
    enlaces = models.URLField(max_length=200, blank=True, null=True)
    localidad = models.CharField(max_length=100, choices=PROVINCE_CHOICES)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100, choices=PROVINCE_CHOICES)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Favorito(models.Model):
    servicio = models.ForeignKey('PerfilEmpresa', on_delete=models.CASCADE, null=True, blank=True)
