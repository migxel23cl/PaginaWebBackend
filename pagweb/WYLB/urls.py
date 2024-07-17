from django.urls import path
from . import views
from .views import lista_productos, crear_producto

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
    path("user_update/", views.user_update, name="user_update"),
    path('gusto/',views.gusto, name="gusto"),
    path('productos/',lista_productos, name="productos"),
    path('feed/', views.feed, name= "feed"),
    path('productoU/',views.productoU, name="productoU"),
    path('perfil/',views.perfil, name="perfil"),
    path('ventanaPago/',views.ventanaPago, name="ventanaPago"),
    path('crearproducto/',crear_producto, name="crear_producto"),
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),
     path('pedidos-pendientes/', views.pedidos_pendientes, name='pedidos_pendientes'),
]
