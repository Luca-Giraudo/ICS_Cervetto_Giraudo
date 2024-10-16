from rest_framework import serializers
from .models import CustomUser, Perfil
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['nombre', 'descripcion', 'enlaces', 'localidad', 'telefono', 'imagen']
        extra_kwargs = {
            'nombre': {'required': False},  # Permitir que sea opcional
            'localidad': {'required': False},  # Permitir que sea opcional
            'telefono': {'required': False},  # Permitir que sea opcional
            'descripcion': {'required': False},
            'enlaces': {'required': False},
            'imagen': {'required': False},
        }

        def update(self, instance, validated_data):
        # Actualiza solo los campos correspondientes, dependiendo del perfil
            if 'descripcion' in validated_data:  # Campo exclusivo de empresa
                instance.descripcion = validated_data.get('descripcion', instance.descripcion)
            if 'enlaces' in validated_data:  # Campo exclusivo de empresa
                instance.enlaces = validated_data.get('enlaces', instance.enlaces)

        # Campos comunes
            instance.nombre = validated_data.get('nombre', instance.nombre)
            instance.localidad = validated_data.get('localidad', instance.localidad)
            instance.telefono = validated_data.get('telefono', instance.telefono)

            instance.save()
            return instance

class CustomUserSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'perfil']

    def update(self, instance, validated_data):
        perfil_data = validated_data.pop('perfil', None)

        # Actualización de PerfilUsuario
        if perfil_data:
            perfil = instance.perfil
            for attr, value in perfil_data.items():
                setattr(perfil, attr, value)
            perfil.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        # Crear el usuario sin establecer el password directamente
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        # Establecer el password usando el método `set_password`
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")
