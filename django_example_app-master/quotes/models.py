from django.db import models
from localflavor.ar.ar_provinces import PROVINCE_CHOICES
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    favoritos = models.ForeignKey('Favorito', on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = CustomUserManager()  # Asigna el CustomUserManager a la clase

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

    def __str__(self):
        return self.email

    class Meta:
        permissions = [
            ("can_view_profile", "Can view profile"),
            ("can_edit_profile", "Can edit profile"),
        ]

class Perfil(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=144)
    enlaces = models.URLField(max_length=200, blank=True, null=True)
    localidad = models.CharField(max_length=100, choices=PROVINCE_CHOICES)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Favorito(models.Model):
    servicio = models.ForeignKey('Perfil', on_delete=models.CASCADE, null=True, blank=True)
