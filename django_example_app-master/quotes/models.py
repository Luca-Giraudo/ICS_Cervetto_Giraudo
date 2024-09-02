from django.db import models
from localflavor.ar.ar_provinces import PROVINCE_CHOICES
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    perfil_empresa = models.ForeignKey('PerfilEmpresa', on_delete=models.CASCADE, null=True, blank=True)
    perfil_usuario = models.ForeignKey('PerfilUsuario', on_delete=models.CASCADE, null=True, blank=True)
    favoritos = models.ForeignKey('Favorito', on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

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
