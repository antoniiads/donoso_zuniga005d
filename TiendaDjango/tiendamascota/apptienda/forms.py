from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Producto, Cliente


class productoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['codigo', 'marca', 'categoria']
        labels ={
            'codigo': 'Codigo', 
            'marca': 'Marca', 
            'categoria': 'Categoria', 
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese codigo', 
                    'id': 'codigo'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'categoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'id': 'Categoria',
                    'placeholder': 'Ingrese categoria', 
                }
            )
        }

class clienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['nombre',  'correo', 'rut']
        labels ={
            'nombre': 'Nombre',  
            'correo': 'Correo',
            'rut': 'Rut'
            
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombre'
                }
            ),  
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su correo', 
                    'id': 'correo'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su rut', 
                    'id': 'rut',
                }
            )

        }