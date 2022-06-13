from django.urls import path
from unicodedata import name 
from .views import form_eliminar, form_producto, index, galeria, somos, api, formulario,  validacion, validacionContacto, ventaproductos, formularioContacto, modificar, ingresoweb, login, form_producto, form_eliminar, MostrarC, ModificarC, AgregarC, form_cliente, form_eliminar_cliente

urlpatterns = [
     path('', index, name="index"),
     path('galeria/', galeria, name="galeria"),
     path('somos/', somos, name="somos" ),
     path('api/', api, name="api" ),
     path('formulario/', formulario, name="formulario"),
     path('formularioContacto/', formularioContacto, name="formularioContacto"),
     path('validacion/', validacion, name="validacion"),
     path('validacionContacto/', validacionContacto, name="validacionContacto"),
     path('ventaproductos/', ventaproductos, name="ventaproductos"),
     path('modificar/<id>', modificar, name="modificar"),
     path('ingresoweb/', ingresoweb,  name="ingresoweb"),
     path('login/', login, name="login"),
     path('agregarproductos/', form_producto, name="agregarproductos"),
     path('modificar/<id>', modificar, name="modificar"),
     path('form_eliminar/<id>', form_eliminar, name="form_eliminar"),
     path('MostrarC/', MostrarC, name="MostrarC"),
     path('ModificarC/<id>', ModificarC, name="ModificarC"),
     path('AgregarC/', AgregarC, name="AgregarC"),
     path('form_cliente/', form_cliente, name="form_cliente"),
     path('form_eliminar_cliente/<id>', form_eliminar_cliente, name="form_eliminar_cliente"),
]         