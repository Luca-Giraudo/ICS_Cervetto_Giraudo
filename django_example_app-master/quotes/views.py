from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, CustomUserSerializer, PerfilSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import Perfil
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'main.html')

def main(request):
    return render(request, 'quotes/main.html')

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class CreateEmpresaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if user.perfil_empresa:
            return Response({"error": "El perfil de empresa ya ha sido creado."}, status=400)

        data = request.data
        serializer = PerfilSerializer(data=data)
        if serializer.is_valid():
            perfil_empresa = serializer.save()
            user.perfil_empresa = perfil_empresa
            user.save()
            return Response({"message": "Perfil de empresa creado exitosamente"}, status=201)
        return Response(serializer.errors, status=400)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener el perfil del usuario autenticado
        user = request.user

        # Verificar si el usuario tiene un perfil, y crearlo si no existe
        if not hasattr(user, 'perfil'):
            perfil = Perfil.objects.create(user=user)
        else:
            perfil = user.perfil

        # Serializar los datos del perfil
        perfil_data = PerfilSerializer(perfil).data
        return Response({'perfil': perfil_data})

    def put(self, request):
        user = request.user
        data = request.data

        # Verificar si el usuario tiene un perfil, y crearlo si no existe
        if not hasattr(user, 'perfil'):
            perfil = Perfil.objects.create(user=user)
        else:
            perfil = user.perfil

        # Actualizar Perfil de Usuario
        serializer = PerfilSerializer(perfil, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Perfil actualizado correctamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class UserDetailAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
