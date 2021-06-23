from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Contacto




# Formulario Usuarios
class CustomUserCreationForm(UserCreationForm):    
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email", "password1", "password2"]



# Formulario Contactos
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        # fields = ["nombre", "correo","tipo_consulta","mensaje","avisos"]
        fields = '__all__'


