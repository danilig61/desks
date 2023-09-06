"""
URL configuration for deskss project.

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('verification/', views.verification, name='verification'),
    path('create/', views.create_advertisement, name='create_advertisement'),
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('private-page/', views.private_page, name='private_page'),
    path('response/<int:pk>/delete/', views.delete_response, name='delete_response'),
    path('response/<int:pk>/accept/', views.accept_response, name='accept_response'),
]

