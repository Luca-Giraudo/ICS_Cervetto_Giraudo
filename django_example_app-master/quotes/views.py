from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, PerfilUsuarioSerializer, PerfilEmpresaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import PerfilUsuario, PerfilEmpresa
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg

def index(request):
    return render(request, 'main.html')

# Registro de usuarios
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

# Login de usuarios
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

# Obtener detalles del usuario
class UserDetailAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Creación y modificación del perfil de usuario
class PerfilUsuarioAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        perfil_usuario = request.user.perfil_usuario
        serializer = PerfilUsuarioSerializer(perfil_usuario)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerfilUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            perfil_usuario = serializer.save()
            request.user.perfil_usuario = perfil_usuario
            request.user.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        perfil_usuario = request.user.perfil_usuario
        serializer = PerfilUsuarioSerializer(perfil_usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Creación y modificación del perfil de empresa
class PerfilEmpresaAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        perfil_empresa = request.user.perfil_empresa
        if perfil_empresa:
            serializer = PerfilEmpresaSerializer(perfil_empresa)
            return Response(serializer.data)
        return Response({"detail": "El usuario no tiene un perfil de empresa"}, status=404)

    def post(self, request):
        if request.user.perfil_empresa:
            return Response({"detail": "El usuario ya tiene un perfil de empresa"}, status=400)
        
        serializer = PerfilEmpresaSerializer(data=request.data)
        if serializer.is_valid():
            perfil_empresa = serializer.save()
            request.user.perfil_empresa = perfil_empresa
            request.user.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        perfil_empresa = request.user.perfil_empresa
        if not perfil_empresa:
            return Response({"detail": "El usuario no tiene un perfil de empresa"}, status=404)

        serializer = PerfilEmpresaSerializer(perfil_empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Consulta de servicios con paginación y ordenación
class ServiciosDisponiblesAPI(generics.ListAPIView):
    serializer_class = PerfilEmpresaSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return PerfilEmpresa.objects.annotate(avg_rating=Avg('favorito__rating')).order_by('-avg_rating')
