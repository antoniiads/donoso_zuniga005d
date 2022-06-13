from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Producto, Cliente 
from .forms import productoForm, clienteForm
# Create your views here.
def index(request):
    return render (request, 'index.html')

def galeria(request):
    return render (request, 'galeria.html') 

def somos (request):
    return render(request, 'somos.html')

def api (request):
    return render(request, 'api.html')   

def formulario(request):
    return render(request, "formulario.html")

def ventaproductos(request):
    return render(request, 'ventaproductos.html')

def validacion(request):
    return render(request, "validacion.html")

def validacionContacto(request):
    return render(request, "validacionContacto.html")  

def formularioContacto(request):
    return render(request, "formularioContacto.html")


def ingresoweb(request):
    return render(request, "ingresoweb.html")

def login(request):
    return render(request, "login.html")


def AgregarC(request):
    return render(request, "AgregarC.html")
    





def ventaproductos(request):
    producto = Producto.objects.all()
 

    datos = {
        'producto' : producto
    }
    return render(request, 'ventaproductos.html', datos)


def form_producto(request): 
    if request.method=='POST':
        producto_form = productoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect ('ventaproductos')
    else:
        producto_form = productoForm()
    return render(request, 'agregarproductos.html', {'producto_form': producto_form})


def modificar(request, id):
    producto = Producto.objects.get(codigo=id)
    datos = {
        'form': productoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = productoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('ventaproductos')
        
    return render(request, 'modificar.html', datos)


def form_eliminar(request,id):
    producto= Producto.objects.get(codigo=id)
    producto.delete()
    return redirect('ventaproductos')

def MostrarC(request):
    cliente = Cliente.objects.all()
 

    datos = {
        'cliente' : cliente
    }
    return render(request, 'MostrarC.html', datos)


def form_cliente(request): 
    if request.method=='POST':
        cliente_form = clienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('MostrarC.html')
    else:
        cliente_form = clienteForm()
    return render(request, 'AgregarC.html', {'cliente_form': cliente_form})


def ModificarC(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': clienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = clienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('MostrarC')
        
    return render(request, 'ModificarC.html', datos)


def form_eliminar_cliente(request,id):
    cliente= Cliente.objects.get(codigo=id)
    cliente.delete()
    return redirect('MostrarC')