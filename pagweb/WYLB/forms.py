from django import forms
from .models import Producto

from django.forms import ModelForm


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'rutaImg1']