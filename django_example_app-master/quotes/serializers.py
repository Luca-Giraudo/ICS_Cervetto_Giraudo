from rest_framework import serializers
from .models import CustomUser, PerfilEmpresa, PerfilUsuario
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ['nombre', 'localidad', 'telefono']

class PerfilEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilEmpresa
        fields = ['nombre', 'descripcion', 'enlaces', 'localidad', 'telefono']

class CustomUserSerializer(serializers.ModelSerializer):
    perfil_usuario = PerfilUsuarioSerializer()
    perfil_empresa = PerfilEmpresaSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'perfil_usuario', 'perfil_empresa']

    def update(self, instance, validated_data):
        perfil_usuario_data = validated_data.pop('perfil_usuario', None)
        perfil_empresa_data = validated_data.pop('perfil_empresa', None)

        # Actualización de PerfilUsuario
        if perfil_usuario_data:
            perfil_usuario = instance.perfil_usuario
            for attr, value in perfil_usuario_data.items():
                setattr(perfil_usuario, attr, value)
            perfil_usuario.save()

        # Actualización o creación de PerfilEmpresa
        if perfil_empresa_data:
            if instance.perfil_empresa:
                perfil_empresa = instance.perfil_empresa
                for attr, value in perfil_empresa_data.items():
                    setattr(perfil_empresa, attr, value)
                perfil_empresa.save()
            else:
                perfil_empresa = PerfilEmpresa.objects.create(**perfil_empresa_data)
                instance.perfil_empresa = perfil_empresa
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
