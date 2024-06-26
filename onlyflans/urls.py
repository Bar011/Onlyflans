"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from web.views import index, about, welcome, contact, success, flan_search
from web import views 
#Importamos las views de la app web

#Creación de las rutas de la app web

urlpatterns = [
    path('admin/', admin.site.urls),
    #El index no tiene un nombre, por ser la pagina principal
    path('', index, name = "index"), 
    path('about/', about, name = "about"),
    path('welcome/', welcome, name = "welcome"),
    path('contact/', contact, name = "contact"),
    path('success/', success, name = "success"),
    path('registration/', include("django.contrib.auth.urls")), #Esto es para las rutas de logueo de Django
    path('flan/<int:flan_id>', views.flan_detail, name = "detail"),
    path('flan_search/', flan_search, name = "search"),
    ]
