from django.urls import path
from . import views
"""
URL configuration for pagweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

urlpatterns=[
    path('',views.index, name="index"),
    path('login.html/',views.login, name="login"),
    path('registro.html/',views.registro, name="registro"),
    path('gustos.html/',views.gustos, name="gustos"),
    path('productos.html/',views.productos, name="productos"),
    path('productoU.html/',views.productoU, name="productoU"),
    path('ventanaPago.html/',views.ventanaPago, name="ventanaPago"),
]
