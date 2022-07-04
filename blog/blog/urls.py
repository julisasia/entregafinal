"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from blog import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from pages.views import listar_pages, inicio, about, crear_page, ver_page, editar_page, eliminar_page
from register.views import login_request, register, logout_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('about/', about),
    path('pages/', listar_pages),
    path('pages/<int:id>/edit', editar_page), 
    path('pages/<int:id>', ver_page),
    path('pages/<int:id>/delete', eliminar_page),
    path("pages/create" , crear_page),
    path("account/login",login_request, name='login_name'),
    path("account/logout",logout_request),
    path("account/signup", register, name = "register" )
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


