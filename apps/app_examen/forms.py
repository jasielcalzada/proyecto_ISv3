from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import maestro

class UserForm(UserCreationForm):
	n_empleado = forms.CharField(max_length=64)
	nombre = forms.CharField(max_length=64)
	correo = forms.CharField(max_length=64)