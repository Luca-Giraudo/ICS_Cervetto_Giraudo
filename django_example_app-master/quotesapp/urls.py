"""quotesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quotes.views import index, main, RegisterAPI, LoginAPI, UserDetailAPI, UserProfileView, UpdateEmpresaProfileView, UpdateProfileView,  listar_perfiles_empresa
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('main/', main),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/user/', UserDetailAPI.as_view(), name='user-detail'),
    path('api/profile/', UserProfileView.as_view(), name='user_profile'),
    path('api/update-empresa/', UpdateEmpresaProfileView.as_view(), name='update_empresa'),
    path('api/update-profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('api/empresas/', listar_perfiles_empresa, name='listar_empresas')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

