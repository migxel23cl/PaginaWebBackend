from django import forms
from .models import Usuario

from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres','apellido','email','password']