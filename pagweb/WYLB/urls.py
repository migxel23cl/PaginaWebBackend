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
    path('quepjeres/',views.quepjeres, name="quepjeres"),
    path('login/',views.login, name="login"),
    path('registro/',views.registro, name="registro"),
    path('gusto/',views.gusto, name="gusto"),
    path('productos/',views.productos, name="productos"),
    path('feed/', views.feed, name= "feed"),
    path('productoU/',views.productoU, name="productoU"),
    path('ventanaPago/',views.ventanaPago, name="ventanaPago"),
]
