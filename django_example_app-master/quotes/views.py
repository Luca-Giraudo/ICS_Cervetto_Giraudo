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
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes

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

class UpdateEmpresaProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            perfil = Perfil.objects.get(user=user, descripcion__isnull=False)
            perfil_data = PerfilSerializer(perfil).data
            return Response({'perfil': perfil_data})
        except Perfil.DoesNotExist:
            return Response({'message': 'No se encontró un perfil de empresa para este usuario'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        user = request.user
        try:
            perfil = Perfil.objects.get(user=user)
        except Perfil.DoesNotExist:
            return Response({'error': 'No existe un perfil asociado a este usuario.'}, status=status.HTTP_404_NOT_FOUND)

        # Actualiza solo los campos de la empresa
        perfil.descripcion = request.data.get('descripcion', perfil.descripcion)
        perfil.enlaces = request.data.get('enlaces', perfil.enlaces)
        perfil.save()

        return Response({'message': 'Perfil de empresa actualizado correctamente'}, status=status.HTTP_200_OK)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            perfil = user.perfil
        except Perfil.DoesNotExist:
            perfil = None

        if perfil:
            perfil_data = PerfilSerializer(perfil).data
            return Response({'perfil': perfil_data})
        else:
            return Response({'message': 'No se encontró un perfil para este usuario'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        user = request.user
        data = request.data
        imagen = request.FILES.get('imagen')  # Obtener la imagen del request

        try:
            perfil = user.perfil
        except Perfil.DoesNotExist:
            perfil = Perfil.objects.create(user=user)  # Crear un perfil si no existe

        perfil_data = {
            'nombre': data.get('nombre', perfil.nombre),
            'localidad': data.get('localidad', perfil.localidad),
            'telefono': data.get('telefono', perfil.telefono),
        }

        if 'descripcion' in data:
            perfil_data['descripcion'] = data.get('descripcion', perfil.descripcion)
            perfil_data['enlaces'] = data.get('enlaces', perfil.enlaces)

        serializer = PerfilSerializer(perfil, data=perfil_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if imagen:  # Guardar la imagen si fue enviada
                perfil.imagen = imagen
                perfil.save()
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

class EmpresaPagination(PageNumberPagination):
    page_size = 3  # Paginación de 3 servicios por página

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_perfiles_empresa(request):
    # Ordenar por nombre alfabéticamente
    perfiles = Perfil.objects.filter(descripcion__isnull=False).order_by('nombre')
    paginator = EmpresaPagination()
    result_page = paginator.paginate_queryset(perfiles, request)
    serializer = PerfilSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
